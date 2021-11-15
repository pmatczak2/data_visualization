import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

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
