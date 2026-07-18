from pathlib import Path
import json
import requests
from bs4 import BeautifulSoup

USERNAME = "abiodunadesesan"

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "data" / "contributions.json"

url = f"https://github.com/users/{USERNAME}/contributions"

response = requests.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    },
    timeout=30
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

days = []

for rect in soup.select("td.ContributionCalendar-day"):

    date = rect.get("data-date")
    count = int(rect.get("data-level", 0))
    contributions = int(rect.get("data-count", 0))

    days.append({
        "date": date,
        "level": count,
        "count": contributions
    })

OUTPUT.parent.mkdir(exist_ok=True)

OUTPUT.write_text(
    json.dumps(days, indent=2)
)

print(f"Saved {len(days)} days")
print(f"Output -> {OUTPUT}")
