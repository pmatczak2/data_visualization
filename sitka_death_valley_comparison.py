import csv
from datetime import datetime
import matplotlib.pyplot as plt

def get_weather_data(filename, dates, highs, lows, date_index, high_index, low_index):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, and high and low temperatures from this file.

