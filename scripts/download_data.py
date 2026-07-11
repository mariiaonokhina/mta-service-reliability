# Imports
from pathlib import Path
import requests
import pandas as pd
import io

# Create data/raw if it doesn't exist
DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents = True, exist_ok = True)

# Save links to download CSV files from NY MTA Open Data
ON_TIME_PERFORMANCE_URL = "https://data.ny.gov/api/views/f6rf-2a3t/rows.csv?accessType=DOWNLOAD"

DELAY_INCIDENTS_URL = "https://data.ny.gov/api/views/g937-7k7c/rows.csv?accessType=DOWNLOAD"

DAILY_RIDERSHIP_2020_2025_URL = "https://data.ny.gov/api/views/vxuj-8kew/rows.csv?accessType=DOWNLOAD"

HOURLY_RIDERSHIP_BASE_URL = "https://data.ny.gov/resource/5wq4-mkjj.csv"

months = [
    ("2026-04-01T00:00:00", "2026-05-01T00:00:00"),
    ("2026-05-01T00:00:00", "2026-06-01T00:00:00"),
    ("2026-06-01T00:00:00", "2026-07-01T00:00:00"),
]

FILES = {
    "on_time_performance.csv": ON_TIME_PERFORMANCE_URL,
    "delay_incidents.csv": DELAY_INCIDENTS_URL,
    "daily_ridership_2020_to_2025.csv": DAILY_RIDERSHIP_2020_2025_URL,
}

# Download and save files into data/dir
for filename, url in FILES.items():
    print(f"Downloading {filename}...")
    response = requests.get(url, timeout = 60)
    response.raise_for_status()

    with open(DATA_DIR / filename, "wb") as f:
        f.write(response.content)

dfs = []

for start, end in months:
    print(f"Downloading {start[:7]}...")
    params = {
        "$where": (
            f"transit_timestamp >= '{start}' "
            f"AND transit_timestamp < '{end}'"
        )
    }

    response = requests.get(
        HOURLY_RIDERSHIP_BASE_URL,
        params=params,
        timeout=120
    )

    response.raise_for_status()
    print(f"URL: {response.url}")
    df = pd.read_csv(io.StringIO(response.text))
    print(f"Downloaded {len(df):,} rows")
    dfs.append(df)

hourly = pd.concat(dfs, ignore_index=True)

outfile = DATA_DIR / "hourly_ridership_select_months.csv"
hourly.to_csv(outfile, index=False)

print(f"Saved {len(hourly):,} rows to {outfile}")
print("Done!")