from pathlib import Path
import csv 
from datetime import datetime
import matplotlib.pyplot as plt

base_path = Path(__file__).parent
file_path = base_path / "weather_data" / "sitka_weather_07-2018_simple.csv"
with open(file_path, 'r') as f:
    contents = f.read()
    contents = contents.rstrip()
    lines = contents.splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)
    print(header_row)
    dates, precips = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    precip = float(row[5])
    dates.append(current_date)
    precips.append(precip)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, precips, color='green')

# Format plot.
ax.set_title("Daily Precipitation, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()