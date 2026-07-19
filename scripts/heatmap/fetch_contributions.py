import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USERNAME = "abiodunadesesan"

url = f"https://github.com/users/{USERNAME}/contributions"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

days = []

for td in soup.select("td.ContributionCalendar-day"):
    date = td.get("data-date")

    if not date:
        continue

    days.append({
        "date": date,
        "level": int(td.get("data-level", 0))
    })

Path("data").mkdir(exist_ok=True)

with open("data/contributions.json", "w") as f:
    json.dump(days, f, indent=2)

print(f"Saved {len(days)} days.")
