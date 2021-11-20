import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 10_000

filename= 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    #  Get dates, brightness, longs, lats.
    dates, brightnesses = [], []
    lats, longs = [], []
    for row in reader:
        current_date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])
        dates.append(current_date)
        brightnesses.append(brightness)


