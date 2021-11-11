import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(filename)
    header_row = next(reader)
    print(header_row)

