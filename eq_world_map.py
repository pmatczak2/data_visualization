import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Making a list of all earthquakes
all_eq_data = all_eq_data['features']
print(len(all_eq_data))

# Extracting Location Data & Extracting Magnitudes
mags, lons, lats = [], [], []
for eq_dict in all_eq_data:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

# Map the Earthquakes
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquake')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')