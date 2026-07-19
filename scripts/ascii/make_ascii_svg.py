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
xmlns:xlink="http://www.w3.org/1999/xlink"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" fill="{BACKGROUND}"/>
""")

svg.append("""
<defs>

<filter id="glow">
<feGaussianBlur stdDeviation="0.5"/>
</filter>

</defs>
""")

# Create multiple frames
for frame in range(3):

    delay = frame * 1.5

    svg.append(f"""
<g opacity="0">
<animate
attributeName="opacity"
values="0;1;1;0"
keyTimes="0;0.05;0.95;1"
dur="4.5s"
begin="{delay}s"
repeatCount="indefinite"/>
""")

    for i, line in enumerate(lines):

        y = 20 + FONT_SIZE + i * LINE_HEIGHT

        svg.append(f"""
<text
x="20"
y="{y}"
font-family="Menlo, Monaco, Consolas, monospace"
font-size="{FONT_SIZE}"
fill="{TEXT_COLOR}"
xml:space="preserve">
{escape(line)}
</text>
""")

    svg.append("</g>")

svg.append("</svg>")

OUTPUT.write_text("".join(svg))

print(f"Generated {OUTPUT}")
