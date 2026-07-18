from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "assets/output/info-card.svg"

WIDTH = 520
HEIGHT = 280

rows = [
    ("Name", "Abiodun Adesesan"),
    ("Role", "Software Engineer"),
    ("Location", "Turkey"),
    ("Stack", "Next.js • React • Node.js"),
    ("Backend", "Express • PostgreSQL"),
    ("Learning", "AI • ML • System Design"),
    ("Editor", "VS Code"),
    ("Terminal", "zsh"),
    ("Faith", "Christian ✝"),
]

svg = []

svg.append(f"""<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}">
""")

svg.append("""
<style>
.title{
font:700 18px monospace;
fill:#58a6ff;
}

.key{
font:700 14px monospace;
fill:#7ee787;
}

.value{
font:14px monospace;
fill:#d0d7de;
}

.line{
opacity:0;
animation:fade .4s forwards;
}

@keyframes fade{
from{
opacity:0;
transform:translateX(-8px);
}
to{
opacity:1;
transform:translateX(0);
}
}
</style>
""")

svg.append("""
<rect width="100%" height="100%" rx="12" fill="#0d1117"/>
<rect x="1" y="1" width="518" height="278"
rx="12"
fill="none"
stroke="#30363d"/>
""")

svg.append("""
<circle cx="24" cy="20" r="6" fill="#ff5f56"/>
<circle cx="44" cy="20" r="6" fill="#ffbd2e"/>
<circle cx="64" cy="20" r="6" fill="#27c93f"/>
""")

svg.append("""
<text
x="90"
y="26"
class="title">
whoami
</text>
""")

y = 60

for i, (key, value) in enumerate(rows):

    svg.append(f"""
<g class="line"
style="animation-delay:{i*0.12}s">

<text
x="30"
y="{y}"
class="key">
{key}
</text>

<text
x="170"
y="{y}"
class="value">
{value}
</text>

</g>
""")

    y += 24

svg.append("</svg>")

OUTPUT.write_text("".join(svg))

print("Generated:", OUTPUT)
