from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[2]

INPUT = ROOT / "assets" / "output" / "profile-prepped.png"
OUTPUT = ROOT / "assets" / "output" / "profile.txt"

ASCII_CHARS = " .:-=+*#%@"

image = Image.open(INPUT)

pixels = image.load()

width, height = image.size

lines = []

for y in range(height):
    line = ""

    for x in range(width):
        pixel = pixels[x, y]

        index = int(pixel / 255 * (len(ASCII_CHARS) - 1))

        line += ASCII_CHARS[index]

    lines.append(line)

ascii_art = "\n".join(lines)

OUTPUT.write_text(ascii_art)

print(ascii_art)

print(f"\nSaved to {OUTPUT}")
