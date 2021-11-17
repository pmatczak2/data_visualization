import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline


# Explore the structure of the data
filename = 'data/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Making a list of all earthquakes
all_eq_data = all_eq_data['features']
print(len(all_eq_data))

# Extracting Location Data & Extracting Magnitudes
# adding Hover text
mags, lons, lats, hover_text = [], [], [], []  # [
for eq_dict in all_eq_data:
    mags.append(eq_dict['properties']['mag'])
    hover_text.append(eq_dict['properties']['title'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])


# Map the Earthquakes
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,  # Customizing Marker Colors
        'colorscale': "Viridis",
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquake')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')