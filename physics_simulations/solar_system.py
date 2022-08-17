import matplotlib.pyplot as plt
from utils import get_horizon_data

nasaids = [1, 2, 3, 4]  # ID numbers in NASA database.
names = ["Mercury", "Venus", "Earth", "Mars"]
colors = ["gray", "orange", "green", "chocolate"]
sizes = [0.38, 0.95, 1.0, 0.53]
texty = [0.47, 0.73, 1, 1.5]
planet_datas = get_horizon_data(nasaids, names, colors, sizes)

# Creating object "ax", which will be a "window" to display an animation.
fig = plt.figure(planet_datas["info"], figsize=[8, 8])
ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))
ax.set_facecolor("black")
plt.legend()
plt.show()
