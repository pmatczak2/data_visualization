import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.
        dates, high, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
            dates.append(current_date)
            dates.append(high)
            dates.append(low)

