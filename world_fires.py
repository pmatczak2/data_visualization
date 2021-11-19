import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename= 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
