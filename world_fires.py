import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

num_rows = 1_000

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    print(header_row)
    #  Get dates, brightness, longs, lats.
    dates, brightnesses = [], []
    lats, lons = [], []
    row_num = 0
    for row in reader:
        date = datetime.strptime(row[5], '%Y-%m-%d')
        brightness = float(row[2])

        dates.append(date)
        brightnesses.append(brightness)
        lats.append(row[0])
        lons.append(row[1])

        row_num += 1
        if row_num == num_rows:
            break

# Map the world fires
data = [{
    'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size': [brightness for brightness in brightnesses],
            'color': brightnesses,
            'colorscale': 'YlOrRd',
            'reversescale': True,
            'colorbar': {'title': 'Brightness'}
        },
}]
my_layout = Layout(title='World Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')


