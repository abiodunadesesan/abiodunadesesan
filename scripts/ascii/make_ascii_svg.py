from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]

INPUT = ROOT / "assets" / "output" / "profile.txt"
OUTPUT = ROOT / "assets" / "output" / "ascii.svg"

lines = INPUT.read_text().splitlines()

font_size = 8
line_height = 10
padding = 20

max_chars = max(len(line) for line in lines)

width = max_chars * 5 + padding * 2
height = len(lines) * line_height + padding * 2

svg = []

svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">
''')

svg.append("""
<rect width="100%" height="100%" fill="#0d1117"/>
""")

svg.append(f'''
<text
x="{padding}"
y="{padding + font_size}"
font-family="monospace"
font-size="{font_size}"
fill="#d0d7de"
xml:space="preserve">
''')

for line in lines:
    svg.append(escape(line))
    svg.append("\n")

svg.append("</text>")
svg.append("</svg>")

OUTPUT.write_text("".join(svg))

print(f"Saved {OUTPUT}")
