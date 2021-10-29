from plotly.graph_objs import Bar, Layout
from plotly import offline

from random_walk import RandomWalk

rw = RandomWalk()

results = []
for walking in range(100):
    result = rw.get_step()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, rw.num_points+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, rw.num_points+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of Random Walk', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')