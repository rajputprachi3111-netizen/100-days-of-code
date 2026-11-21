
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

# Canvas
W, H = 1920, 1080
img = Image.new("RGB", (W, H), (35, 12, 35))
draw = ImageDraw.Draw(img)

# Gradient background
for y in range(H):
    t = y / H
    color = (
        int(35 + 75 * t),
        int(12 + 12 * t),
        int(35 + 40 * t)
    )
    draw.line((0, y, W, y), fill=color)

# Decorative stars
for _ in range(180):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(1, 3)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255, 150, 205))

# Cherry blossom petals
for _ in range(100):
    x = random.randint(0, W)
    y = random.randint(0, H)
    r = random.randint(5, 13)
    draw.ellipse(
        (x-r, y-r, x+r, y+r),
        fill=(255, random.randint(100, 190), 200)
    )

# Neon text glow
glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)

font_path = r"C:\Windows\Fonts\segoesc.ttf"

try:
    title_font = ImageFont.truetype(font_path, 125)
    subtitle_font = ImageFont.truetype(font_path, 75)
except OSError:
    title_font = ImageFont.truetype(
        r"C:\Windows\Fonts\arial.ttf", 110
    )
    subtitle_font = title_font

lines = [
    ("The Angry", title_font, 320),
    ("East Indian", title_font, 475),
    ("Off Topic ♡", subtitle_font, 640)
]

for text, font, y in lines:
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (W - text_width) // 2

    # Pink glow
    glow_draw.text(
        (x, y), text,
        font=font,
        fill=(255, 50, 160, 255),
        stroke_width=12
    )

    draw.text(
        (x, y), text,
        font=font,
        fill=(255, 220, 240),
        stroke_width=2,
        stroke_fill=(255, 80, 170)
    )

# Blur and blend glow
glow = glow.filter(ImageFilter.GaussianBlur(25))
img = Image.alpha_composite(
    img.convert("RGBA"), glow
)

draw = ImageDraw.Draw(img)

# Decorative underline
draw.arc(
    (400, 700, 1520, 850),
    start=10,
    end=170,
    fill=(255, 120, 200),
    width=8
)

# Small decorative hearts
for x, y in [(300, 300), (1600, 350), (350, 750), (1580, 780)]:
    draw.text((x, y), "♡", fill=(255, 150, 210))

# Footer
footer_font = ImageFont.truetype(
    r"C:\Windows\Fonts\arial.ttf", 32
)
draw.text(
    (720, 950),
    "LIKE  •  SHARE  •  SUBSCRIBE",
    font=footer_font,
    fill=(255, 190, 220)
)

# Save
img.convert("RGB").save(
    "the_angry_east_indian_off_topic.png"
)

print("Your aesthetic YouTube artwork is ready!")
