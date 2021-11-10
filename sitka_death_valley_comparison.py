import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            try:
                high = int(row[high_index])
                low = int(row[low_index])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# Get weather data for Sitka
file_name = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
get_weather_data(file_name, dates, highs, lows, date_index=2, high_index=5, low_index=6)

# Plot Sitka weather data.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)