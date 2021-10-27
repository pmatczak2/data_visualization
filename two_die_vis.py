from plotly.graph_objs import Bar, Layout
from plotly import offline

from two_D8 import TwoD8

die_1 = TwoD8()
die_2 = TwoD8()



# Make some rolls, and store results in a list
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analyze the results.
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Results', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Result of rolling three D8 die 1_000_000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3d8.html')