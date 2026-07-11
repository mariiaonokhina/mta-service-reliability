# MTA Service Reliability 

## Datasets
**Primary:**
1. https://data.ny.gov/Transportation/MTA-Subway-Terminal-On-Time-Performance-Beginning-/f6rf-2a3t/about_data
2. https://data.ny.gov/Transportation/MTA-Subway-Delay-Causing-Incidents-Beginning-2020/g937-7k7c/about_data
3. https://data.ny.gov/Transportation/MTA-Subway-Hourly-Ridership-Beginning-2025/5wq4-mkjj/about_data

**Additional:**
* https://www.ncei.noaa.gov/cdo-web/datasets (Daily Summaries)
* U.S. Federal Holidays (Created programmatically)

---
## How to Run
1. Clone this repository by running `git clone https://github.com/mariiaonokhina/mta-service-reliability.git`.
2. Go into the repository folder by running `cd mta-service-reliability.git`.
3. Create a virtual environment: `python -m venv .venv` and activate it: `source .venv/bin/activate` (for Mac).
4. Install the requirements: `pip install -r requirements.txt`
5. Download MTA data by running `python scripts/download_data.py`.
6. Open and run `notebooks/01_inspection.ipynb`.
7. Open and run `notebooks/02_analysis.ipynb`.
