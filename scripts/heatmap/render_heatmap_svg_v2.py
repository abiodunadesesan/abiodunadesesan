import json
from pathlib import Path

BOX = 10
GAP = 3
LEFT = 35
TOP = 25

COLORS = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

MONTHS = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]

DAYS = ["Mon", "Wed", "Fri"]

days = json.load(open("data/contributions.json"))
weeks = [days[i:i + 7] for i in range(0, len(days), 7)]

width = LEFT + len(weeks) * (BOX + GAP) + 30
height = TOP + 7 * (BOX + GAP) + 60

svg = f"""<svg
xmlns="http://www.w3.org/2000/svg"
width="{width}"
height="{height}"
viewBox="0 0 {width} {height}">

<style>

svg {{
    background:#0d1117;
}}

text {{
    fill:#8b949e;
    font-family:ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-size:11px;
}}

rect {{
    rx:2.5;
}}

</style>

<rect
x="0"
y="0"
width="{width}"
height="{height}"
fill="#0d1117"/>

"""
svg += "</svg>"

Path("assets/output").mkdir(parents=True, exist_ok=True)

with open("assets/output/contrib-heatmap-v2.svg", "w") as f:
    f.write(svg)

print("Generated contrib-heatmap-v2.svg")
svg += "</svg>"
# Weekday labels
label_positions = [
    ("Mon", 1),
    ("Wed", 3),
    ("Fri", 5),
]

for label, row in label_positions:
    y = TOP + row * (BOX + GAP) + BOX - 1
    svg += f'''
<text
x="5"
y="{y}">
{label}
</text>
'''
delay = 0

for week_index, week in enumerate(weeks):

    for day_index, day in enumerate(week):

        x = LEFT + week_index * (BOX + GAP)
        y = TOP + day_index * (BOX + GAP)

        level = min(day["level"], 4)
        color = COLORS[level]

        svg += f"""
<rect
x="{x}"
y="{y}"
width="{BOX}"
height="{BOX}"
fill="{color}">
<animate
attributeName="opacity"
from="0"
to="1"
dur="0.25s"
begin="{delay}ms"
fill="freeze"/>
</rect>
"""

        delay += 6
