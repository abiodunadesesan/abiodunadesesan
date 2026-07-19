from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]

INPUT = ROOT / "assets/output/profile.txt"
OUTPUT = ROOT / "assets/output/avi-ascii.svg"

FONT_SIZE = 8
LINE_HEIGHT = 10

TEXT_COLOR = "#d0d7de"
BACKGROUND = "#0d1117"

lines = INPUT.read_text().splitlines()

max_chars = max(len(line) for line in lines)

width = max_chars * 5 + 40
height = len(lines) * LINE_HEIGHT + 40

svg = []

svg.append(f"""
<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<rect width="100%" height="100%" fill="{BACKGROUND}"/>
""")

svg.append("""
<style>
.ascii {
animation: show 5s infinite;
}
@keyframes show {
0% { opacity:0; }
15% { opacity:1; }
85% { opacity:1; }
100% { opacity:0; }
}
</style>
""")

svg.append("""
<g class="ascii">
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

svg.append("""
</g>
</svg>
""")

OUTPUT.write_text("".join(svg))

print(f"Generated {OUTPUT}")
