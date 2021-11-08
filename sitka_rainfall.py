import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get date and rainfall from this file.
    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = [4]
        dates.append(current_date)
        rainfalls.append(rainfall)

# Plot the high temperature
plt.style.use('seaborn')
fig, ax = plt.subplots()
sx.plot(dates, rainfalls, c='blue')

# Format plot
ax.set_title("Daily rainfall for 2018", fontsize=24)
ax.set_xlabel('', fontsizw=16)
fig.autofmt_xdate()