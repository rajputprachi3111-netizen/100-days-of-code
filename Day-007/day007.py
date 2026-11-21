
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import math

WIDTH, HEIGHT = 1920, 1080
random.seed(7)

# Black background
img = Image.new("RGB", (WIDTH, HEIGHT), (2, 3, 10))
draw = ImageDraw.Draw(img)

# Dark blue-green gradient
for y in range(HEIGHT):
    for x in range(WIDTH):
        glow = math.exp(
            -((x - 960)**2 + (y - 480)**2) / 700000
        )
        img.putpixel(
            (x, y),
            (
                int(2 + glow * 3),
                int(3 + glow * 18),
                int(10 + glow * 35)
            )
        )

draw = ImageDraw.Draw(img)

# Matrix-style falling code
matrix_font = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf", 19
)

chars = "01ABCDEF<>#$%&"

for x in range(25, WIDTH, 32):
    start = random.randint(-400, 700)

    for i in range(30):
        y = start + i * 30
        if 0 <= y < HEIGHT:
            draw.text(
                (x, y),
                random.choice(chars),
                font=matrix_font,
                fill=(0, random.randint(60, 150), 60)
            )

# Futuristic circuit lines
for i in range(45):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    length = random.randint(70, 220)

    points = [
        (x, y),
        (x + length, y),
        (x + length, y + 35),
        (x + length + 45, y + 35)
    ]

    draw.line(points, fill=(0, 130, 180), width=2)

    draw.ellipse(
        (x - 4, y - 4, x + 4, y + 4),
        fill=(0, 255, 180)
    )

# Digital particles
for i in range(250):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    draw.ellipse(
        (x, y, x + 2, y + 2),
        fill=(0, random.randint(120, 255), 200)
    )

# Fonts
title_font = ImageFont.truetype(
    "C:/Windows/Fonts/consolab.ttf", 112
)

subtitle_font = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf", 30
)

small_font = ImageFont.truetype(
    "C:/Windows/Fonts/consola.ttf", 22
)

# Main title
line1 = "THE ANGRY"
line2 = "EAST INDIAN"

def center_x(text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return (WIDTH - (bbox[2] - bbox[0])) // 2

# Neon glow
glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
gd = ImageDraw.Draw(glow)

gd.text(
    (center_x(line1, title_font), 365),
    line1, font=title_font, fill=(0, 255, 120, 255)
)

gd.text(
    (center_x(line2, title_font), 500),
    line2, font=title_font, fill=(0, 180, 255, 255)
)

glow = glow.filter(ImageFilter.GaussianBlur(28))
img = Image.alpha_composite(img.convert("RGBA"), glow)

draw = ImageDraw.Draw(img)

# Main title
draw.text(
    (center_x(line1, title_font), 365),
    line1,
    font=title_font,
    fill=(220, 255, 230),
    stroke_width=2,
    stroke_fill=(0, 255, 120)
)

draw.text(
    (center_x(line2, title_font), 500),
    line2,
    font=title_font,
    fill=(220, 245, 255),
    stroke_width=2,
    stroke_fill=(0, 180, 255)
)

# Subtitle
def centered(text, y, font, color):
    x = center_x(text, font)
    draw.text((x, y), text, font=font, fill=color)

centered(
    "> THINK. CREATE. SECURE.",
    680,
    subtitle_font,
    (0, 255, 150)
)

centered(
    "ARTIFICIAL INTELLIGENCE  |  CYBERSECURITY  |  INNOVATION",
    740,
    small_font,
    (0, 190, 230)
)

# Border
draw.rounded_rectangle(
    (45, 45, WIDTH - 45, HEIGHT - 45),
    radius=25,
    outline=(0, 210, 150),
    width=3
)

# Corner labels
draw.text(
    (85, 85), "SYSTEM://FUTURE",
    font=small_font, fill=(0, 255, 150)
)

draw.text(
    (WIDTH - 350, 85), "AI_SECURITY.exe",
    font=small_font, fill=(0, 190, 255)
)

centered(
    "DAY 007  |  100 DAYS OF CODE",
    940,
    small_font,
    (140, 180, 200)
)

# Save image
output = "the_angry_east_indian_day007.png"
img.convert("RGB").save(output)

print("Day 007 artwork generated successfully!")
print(f"Saved as: {output}")
