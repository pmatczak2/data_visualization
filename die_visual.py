from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# create two D6 dice.
die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results .append(result)

# analyze the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the result
x_values = list(range(2, max_result+1)) # plotly doesn't accept range() function directly, convert to list() function
data = [Bar(x=x_values, y=frequencies)]  # Bar() represents a data set that will be formatted as whole

x_axis_config = {'title': 'Result', 'dtick': 1} # Layout() returns object specified, configuration of the graph as a whole
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D10 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config) # Set the title of graph, configuration dictionary
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html') # offline.plot need dictionary containing the data
            #and also accepts a dictionary containing the data and layout objects also the name where file will be saved
print(frequencies)