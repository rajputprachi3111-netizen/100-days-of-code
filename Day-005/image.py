from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

WIDTH, HEIGHT = 1080, 1080
TITLE = "The Angry East Indian\nOff Topic"
FONT_PATH = "handwriting.ttf"
FONT_SIZE = 110
TEXT_COLOR = (120, 40, 60)
OUTPUT = "angry_east_indian_off_topic.png"

img = Image.new("RGB", (WIDTH, HEIGHT), (255, 240, 235))
draw = ImageDraw.Draw(img)

top_color = (255, 228, 225)
mid_color = (255, 214, 194)
bottom_color = (255, 245, 235)

for y in range(HEIGHT):
    t = y / HEIGHT
    if t < 0.5:
        k = t / 0.5
        r = int(top_color[0]*(1-k) + mid_color[0]*k)
        g = int(top_color[1]*(1-k) + mid_color[1]*k)
        b = int(top_color[2]*(1-k) + mid_color[2]*k)
    else:
        k = (t - 0.5) / 0.5
        r = int(mid_color[0]*(1-k) + bottom_color[0]*k)
        g = int(mid_color[1]*(1-k) + bottom_color[1]*k)
        b = int(mid_color[2]*(1-k) + bottom_color[2]*k)
    draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

blob_layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
bdraw = ImageDraw.Draw(blob_layer)

random.seed(7)
for _ in range(18):
    cx = random.randint(0, WIDTH)
    cy = random.randint(0, HEIGHT)
    rad = random.randint(120, 320)
    color = random.choice([
        (255, 182, 193, 55),
        (255, 218, 185, 45),
        (230, 190, 255, 40),
        (255, 240, 245, 60),
    ])
    bdraw.ellipse([cx-rad, cy-rad, cx+rad, cy+rad], fill=color)

blob_layer = blob_layer.filter(ImageFilter.GaussianBlur(radius=80))
img = Image.alpha_composite(img.convert("RGBA"), blob_layer).convert("RGB")

draw = ImageDraw.Draw(img, "RGBA")
for _ in range(140):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.choice([1, 1, 1, 2, 2, 3])
    alpha = random.randint(60, 160)
    draw.ellipse([x-r, y-r, x+r, y+r], fill=(212, 175, 120, alpha))

for _ in range(10):
    x = random.randint(80, WIDTH-80)
    y = random.randint(80, HEIGHT-80)
    s = random.randint(8, 16)
    draw.line([(x-s, y), (x+s, y)], fill=(212, 175, 120, 170), width=2)
    draw.line([(x, y-s), (x, y+s)], fill=(212, 175, 120, 170), width=2)
font_size = FONT_SIZE
font = ImageFont.truetype(FONT_PATH, font_size)

while True:
    lines = TITLE.split("\n")
    max_line_width = 0
    line_heights = []
    line_widths = []
    
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        line_widths.append(w)
        line_heights.append(h)
        if w > max_line_width:
            max_line_width = w
            
    if max_line_width < (WIDTH - 150):
        break
    font_size -= 5
    font = ImageFont.truetype(FONT_PATH, font_size)

total_h = sum(line_heights) + (len(lines) - 1) * 30
start_y = (HEIGHT - total_h) // 2 - 40
total_h = sum(line_heights) + (len(lines) - 1) * 30
start_y = (HEIGHT - total_h) // 2 - 40

shadow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
sdraw = ImageDraw.Draw(shadow)
y = start_y
for i, line in enumerate(lines):
    x = (WIDTH - line_widths[i]) // 2
    sdraw.text((x+4, y+6), line, font=font, fill=(120, 60, 80, 90))
    y += line_heights[i] + 30
shadow = shadow.filter(ImageFilter.GaussianBlur(6))
img = Image.alpha_composite(img.convert("RGBA"), shadow).convert("RGB")

draw = ImageDraw.Draw(img)
y = start_y
for i, line in enumerate(lines):
    x = (WIDTH - line_widths[i]) // 2
    draw.text((x, y), line, font=font, fill=TEXT_COLOR)
    y += line_heights[i] + 30

draw.rectangle(
    [30, 30, WIDTH-30, HEIGHT-30],
    outline=(212, 175, 120, 200),
    width=3
)
draw.rectangle(
    [42, 42, WIDTH-42, HEIGHT-42],
    outline=(212, 175, 120, 90),
    width=1
)

img.save(OUTPUT, "PNG", quality=95)
print(f"Saved as {OUTPUT}")
img.show()