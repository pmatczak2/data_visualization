import json

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

# Extracting Magnitudes
mags = []
for all_eq_data in all_eq_data:
    mag = all_eq_data['properties']['mag']
    mags.append(mag)

print(mags[:10])