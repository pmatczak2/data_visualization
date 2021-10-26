from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
for roll_num in range(1000):
    result = die.roll()
    results .append(result)

# analyze the result
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize the result
x_values = list(range(1, die.num_sides+1)) # plotly doesn't accept range() function directly, convert to list() function
data = [Bar(x=x_values, y=frequencies)]  # Bar() represents a data set that will be formatted as whole

x_axis_config = {'title': 'Result'} # Layout() returns object specified, configuration of the graph as a whole
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling on D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config) # Set the title of graph, configuration dictionary
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html') # offline.plot need dictionary containing the data
            #and also accepts a dictionary containing the data and layout objects also the name where file will be saved
print(frequencies)