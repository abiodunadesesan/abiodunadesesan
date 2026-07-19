import json
from pathlib import Path

BOX = 13
GAP = 4

COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

days = json.load(open("data/contributions.json"))

weeks = []

for i in range(0, len(days), 7):
    weeks.append(days[i:i+7])

width = len(weeks) * (BOX + GAP) + 40
height = 7 * (BOX + GAP) + 80

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}"
style="background:#0d1117">

<style>

rect{{
rx:3;
animation:pop .5s ease forwards;
opacity:0;
}}

@keyframes pop{{
from{{opacity:0;transform:translateY(8px)}}
to{{opacity:1;transform:translateY(0)}}
}}

text{{
fill:#8b949e;
font-family:monospace;
font-size:12px;
}}

</style>

'''

delay = 0

for x, week in enumerate(weeks):

    for y, day in enumerate(week):

        color = COLORS[min(day["level"], 4)]

        xpos = 30 + x * (BOX + GAP)
        ypos = 20 + y * (BOX + GAP)

        svg += f'''
<rect
x="{xpos}"
y="{ypos}"
width="{BOX}"
height="{BOX}"
fill="{color}"
style="animation-delay:{delay}ms"/>
'''

        delay += 6

svg += f'''

<text x="30" y="{height-20}">
GitHub Contributions • {len(days)} days
</text>

</svg>
'''

Path("assets/output").mkdir(parents=True, exist_ok=True)

with open("assets/output/contrib-heatmap.svg","w") as f:
    f.write(svg)

print("Generated contrib-heatmap.svg")
