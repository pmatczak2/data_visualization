from plotly.graph_objs import Bar, Layout
from plotly import offline

from two_D8 import TwoD8

die_1 = TwoD8()
die_2 = TwoD8()

# Make some rolls, and store results in a list
results = []
for roll_num in range(10_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analize the results.
frequencies = []
max_result = die_1.num_sides = die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

