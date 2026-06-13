# 

# Imports
from pathlib import Path
import requests

# Create data/raw if it doesn't exist
DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents = True, exist_ok = True)

# Save links to download CSV files from NY MTA Open Data
ON_TIME_PERFORMANCE_URL = "https://data.ny.gov/api/views/f6rf-2a3t/rows.csv?accessType=DOWNLOAD"

DELAY_INCIDENTS_URL = "https://data.ny.gov/api/views/g937-7k7c/rows.csv?accessType=DOWNLOAD"

FILES = {
    "on_time_performance.csv": ON_TIME_PERFORMANCE_URL,
    "delay_incidents.csv": DELAY_INCIDENTS_URL
}

# Download and save files into data/dir
for filename, url in FILES.items():
    print(f"Downloading {filename}...")
    response = requests.get(url, timeout = 60)
    response.raise_for_status()

    with open(DATA_DIR / filename, "wb") as f:
        f.write(response.content)

print("Done!")