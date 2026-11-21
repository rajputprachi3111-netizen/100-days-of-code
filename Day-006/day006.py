
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import random

WIDTH, HEIGHT = 1080, 1080
random.seed(42)

img = Image.new("RGB", (WIDTH, HEIGHT), (5, 8, 25))
draw = ImageDraw.Draw(img)

for y in range(HEIGHT):
    for x in range(WIDTH):
        glow = math.exp(
            -((x - 1350)**2 + (y - 450)**2) / 500000
        )
        r = int(5 + glow * 15)
        g = int(8 + glow * 20)
        b = int(25 + glow * 75)

        img.putpixel((x, y), (r, g, b))

draw = ImageDraw.Draw(img)

for x in range(0, WIDTH, 80):
    draw.line(
        (x, 0, x, HEIGHT),
        fill=(15, 35, 65),
        width=1
    )

for y in range(0, HEIGHT, 80):
    draw.line(
        (0, y, WIDTH, y),
        fill=(15, 35, 65),
        width=1
    )

for i in range(35):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    length = random.randint(80, 250)

    points = [
        (x, y),
        (x + length // 2, y),
        (x + length // 2, y + 40),
        (x + length, y + 40)
    ]

    draw.line(points, fill=(0, 180, 255), width=2)
    draw.ellipse(
        (x - 4, y - 4, x + 4, y + 4),
        fill=(0, 255, 255)
    )

for i in range(180):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    radius = random.choice([1, 2, 3])

    draw.ellipse(
        (x, y, x + radius, y + radius),
        fill=(0, random.randint(150, 255), 255)
    )

draw.rounded_rectangle(
    (65, 65, WIDTH - 65, HEIGHT - 65),
    radius=30,
    outline=(0, 180, 255),
    width=3
)

font_path = "C:/Windows/Fonts/arialbd.ttf"
small_font_path = "C:/Windows/Fonts/arial.ttf"

title_font = ImageFont.truetype(font_path, 125)
subtitle_font = ImageFont.truetype(small_font_path, 32)
tag_font = ImageFont.truetype(font_path, 25)

title = "THE ANGRY"
title2 = "EAST INDIAN"

bbox1 = draw.textbbox((0, 0), title, font=title_font)
bbox2 = draw.textbbox((0, 0), title2, font=title_font)

text_width1 = bbox1[2] - bbox1[0]
text_width2 = bbox2[2] - bbox2[0]

x1 = (WIDTH - text_width1) // 2
x2 = (WIDTH - text_width2) // 2

glow = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
glow_draw = ImageDraw.Draw(glow)

glow_draw.text(
    (x1, 365), title,
    font=title_font,
    fill=(0, 200, 255, 255),
    stroke_width=4,
    stroke_fill=(0, 100, 255, 255)
)

glow_draw.text(
    (x2, 510), title2,
    font=title_font,
    fill=(180, 70, 255, 255),
    stroke_width=4,
    stroke_fill=(100, 0, 255, 255)
)

glow = glow.filter(ImageFilter.GaussianBlur(25))
img = Image.alpha_composite(img.convert("RGBA"), glow)

draw = ImageDraw.Draw(img)

draw.text(
    (x1, 365), title,
    font=title_font,
    fill=(230, 250, 255),
    stroke_width=2,
    stroke_fill=(0, 180, 255)
)

draw.text(
    (x2, 510), title2,
    font=title_font,
    fill=(255, 255, 255),
    stroke_width=2,
    stroke_fill=(170, 60, 255)
)

subtitle = "FUTURE IS BUILT BY THE FEARLESS"

bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
subtitle_width = bbox[2] - bbox[0]

draw.text(
    ((WIDTH - subtitle_width) // 2, 700),
    subtitle,
    font=subtitle_font,
    fill=(0, 220, 255)
)

footer = "DAY 006  |  100 DAYS OF CODE"

bbox = draw.textbbox((0, 0), footer, font=tag_font)
footer_width = bbox[2] - bbox[0]

draw.text(
    ((WIDTH - footer_width) // 2, 920),
    footer,
    font=tag_font,
    fill=(180, 190, 220)
)

img.convert("RGB").save(
    "the_angry_east_indian_day006.png",
    quality=100
)

print("Image generated successfully!")
