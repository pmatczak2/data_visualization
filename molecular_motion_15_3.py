import matplotlib.pyplot as plt
from random_walk import RandomWalk

#while True:
rw = RandomWalk()
rw.fill_walk()

plt.style.use('seaborn')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, s=1)

#ax.get_xaxis().set_visible(False)
#ax.get_yaxis().set_visible(False)

plt.show()

    #keep_running = input("Make another walk? (y/n): ")
    #if keep_running == 'n':
    #   break
