from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]

INPUT = ROOT / "assets/output/profile.txt"
OUTPUT = ROOT / "assets/output/avi-ascii.svg"

FONT_SIZE = 8
LINE_HEIGHT = 10
CHAR_WIDTH = 5

TEXT_COLOR = "#d0d7de"
BACKGROUND = "#0d1117"

lines = INPUT.read_text().splitlines()

max_chars = max(len(line) for line in lines)

width = max_chars * CHAR_WIDTH + 40
height = len(lines) * LINE_HEIGHT + 40

svg = []

svg.append(f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" fill="{BACKGROUND}"/>
""")

svg.append("<defs>")

for i, line in enumerate(lines):
    w = max(len(line) * CHAR_WIDTH, 1)

    svg.append(f"""
<clipPath id="clip{i}">
<rect
x="20"
y="{20 + i*LINE_HEIGHT - FONT_SIZE}"
width="0"
height="{LINE_HEIGHT}">
<animate
attributeName="width"
from="0"
to="{w}"
begin="{i*0.05}s"
dur="0.45s"
fill="freeze"
repeatCount="indefinite"/>
</rect>
</clipPath>
""")

svg.append("</defs>")

for i, line in enumerate(lines):

    y = 20 + FONT_SIZE + i * LINE_HEIGHT

    svg.append(f"""
<text
clip-path="url(#clip{i})"
x="20"
y="{y}"
font-family="Menlo, Monaco, Consolas, monospace"
font-size="{FONT_SIZE}"
fill="{TEXT_COLOR}"
xml:space="preserve">
{escape(line)}
</text>
""")

svg.append("</svg>")

OUTPUT.write_text("".join(svg))

print(f"Generated {OUTPUT}")
