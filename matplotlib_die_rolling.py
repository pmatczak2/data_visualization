import matplotlib.pyplot as plt

from two_D8 import TwoD8

die_1 = TwoD8()
die_2 = TwoD8()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

td = TwoD8()
td.roll()

plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(results, results, s=15)