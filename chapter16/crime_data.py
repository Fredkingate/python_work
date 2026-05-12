from collections import Counter
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

base_path = Path(__file__).parent
file_path = base_path / "Crime_Data_from_2020_to_2024.csv"

crime_months = Counter()
crime_areas = Counter()
crime_types = Counter()

with file_path.open("r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        date_str = row.get("DATE OCC", "").strip()
        area_name = row.get("AREA NAME", "Unknown").strip() or "Unknown"
        crime_desc = row.get("Crm Cd Desc", "Unknown").strip() or "Unknown"

        try:
            date_occ = datetime.strptime(date_str, "%m/%d/%Y %I:%M:%S %p")
        except ValueError:
            continue

        month_label = date_occ.strftime("%Y-%m")
        crime_months[month_label] += 1
        crime_areas[area_name] += 1
        crime_types[crime_desc] += 1

if not crime_months:
    raise SystemExit("No valid crime records were parsed from the CSV.")

# Prepare data for plotting
sorted_months = sorted(crime_months)
month_counts = [crime_months[month] for month in sorted_months]

top_areas = crime_areas.most_common(10)
area_names, area_counts = zip(*top_areas)

top_types = crime_types.most_common(10)
crime_names, crime_counts = zip(*top_types)

plt.style.use("seaborn-v0_8")
fig, axes = plt.subplots(3, 1, figsize=(12, 18), constrained_layout=True)

axes[0].plot(sorted_months, month_counts, marker="o", linewidth=2)
axes[0].set_title("Monthly Crime Reports (2020-2024)", fontsize=18)
axes[0].set_xlabel("Month", fontsize=14)
axes[0].set_ylabel("Number of Crimes", fontsize=14)
axes[0].tick_params(axis="x", rotation=45, labelsize=10)

axes[1].barh(area_names[::-1], area_counts[::-1], color="tab:blue")
axes[1].set_title("Top 10 Areas by Crime Count", fontsize=18)
axes[1].set_xlabel("Number of Crimes", fontsize=14)
axes[1].set_ylabel("Area Name", fontsize=14)
axes[1].tick_params(labelsize=12)

axes[2].barh(crime_names[::-1], crime_counts[::-1], color="tab:orange")
axes[2].set_title("Top 10 Crime Types", fontsize=18)
axes[2].set_xlabel("Number of Crimes", fontsize=14)
axes[2].set_ylabel("Crime Description", fontsize=14)
axes[2].tick_params(labelsize=12)

fig.suptitle("Crime Data Analysis", fontsize=24)
plt.savefig(base_path / "crime_data_summary.png")
plt.show()
