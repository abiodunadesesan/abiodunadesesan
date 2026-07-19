import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("data/contributions.json")
OUTPUT = Path("assets/output/contrib-heatmap.svg")

CELL = 12
GAP = 3

LEFT = 35
TOP = 35

COLS = 53
ROWS = 7

WIDTH = LEFT + COLS * (CELL + GAP) + 40
HEIGHT = TOP + ROWS * (CELL + GAP) + 90

PALETTE = [
    "#161b22",
    "#0e4429",
    "#006d32",
    "#26a641",
    "#39d353",
]

with open(DATA_FILE) as f:
    days = json.load(f)

days = sorted(
    days,
    key=lambda x: datetime.strptime(x["date"], "%Y-%m-%d")
)

total = 0
current_streak = 0
longest_streak = 0

running = 0

for day in days:
    if day["level"] > 0:
        total += 1
        running += 1
        longest_streak = max(longest_streak, running)
    else:
        running = 0

for day in reversed(days):
    if day["level"] > 0:
        current_streak += 1
    else:
        break

svg = []

svg.append(f'''<svg xmlns="http://www.w3.org/2000/svg"
width="{WIDTH}"
height="{HEIGHT}"
viewBox="0 0 {WIDTH} {HEIGHT}"
style="background:#0d1117">

<rect width="100%" height="100%" fill="#0d1117"/>

<text x="20" y="20"
fill="#c9d1d9"
font-family="monospace"
font-size="14"
font-weight="bold">
GitHub Contributions
</text>
''')
for index, day in enumerate(days):

    week = index // 7
    weekday = index % 7

    x = LEFT + week * (CELL + GAP)
    y = TOP + weekday * (CELL + GAP)

    color = PALETTE[min(day["level"], 4)]

    svg.append(f'''
<rect
x="{x}"
y="{y}"
width="{CELL}"
height="{CELL}"
rx="2"
fill="{color}"/>
''')
svg.append(f"""
<text
x="20"
y="{HEIGHT-25}"
fill="#8b949e"
font-size="12"
font-family="monospace">
Active days: {total}
</text>

<text
x="170"
y="{HEIGHT-25}"
fill="#8b949e"
font-size="12"
font-family="monospace">
Current streak: {current_streak}
</text>

<text
x="360"
y="{HEIGHT-25}"
fill="#8b949e"
font-size="12"
font-family="monospace">
Longest streak: {longest_streak}
</text>

</svg>
""")
OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with open(OUTPUT, "w") as f:
    f.write("\n".join(svg))

print("Saved:", OUTPUT)
