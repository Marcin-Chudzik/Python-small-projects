from datetime import datetime, timedelta

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

from utils import get_horizon_data


class CosmicObject:  # Class for defining cosmic objects.
    def __init__(self, name, rad, color, r, v):
        self.name = name
        self.r = np.array(r, dtype=np.float64)  # Vectors of distance radius from the Sun.
        self.v = np.array(v, dtype=np.float64)  # Vectors of speed relative to the Sun.
        self.xs = []  # Subsequent x items
        self.ys = []  # Subsequent y items
        # Properties referencing to the window with animation.
        self.plot = ax.scatter(r[0], r[1], color=color, s=rad ** 2, edgecolor=None, zorder=10)
        (self.line,) = ax.plot([], [], color=color, linewidth=1.4)


class SolarSystem:
    def __init__(self):
        self.planets = []
        self.time = None
        # Properties
        self.timestamp = ax.text(0.03, 0.94, "Data: ", color="w", transform=ax.transAxes, fontsize="x-large")

    def add_planet(self, planet):
        # Adding a planet to graph
        self.planets.append(planet)

    def evolve(self):
        # Calculating a successive points of trajectory.
        dt = 1
        self.time += timedelta(dt)
        plots = []
        lines = []
        for i, planet in enumerate(self.planets):
            # Calculating a successive radius vectors.
            planet.r += planet.v * dt
            acc = -2.959e-4 * planet.r / np.sum(planet.r ** 2) ** (3 / 2)  # planet acceleration
            planet.v += acc * dt
            planet.xs.append(planet.r[0])
            planet.ys.append(planet.r[1])
            # Adding next element of graph animation.
            planet.plot.set_offsets(planet.r[:2])
            plots.append(planet.plot)
            planet.line.set_xdata(planet.xs)
            planet.line.set_ydata(planet.ys)
            # Adding another part of line.
            lines.append(planet.line)
        # Setting limit of positions to safe from too big amount of calculate.
        if len(planet.xs) > 10000:
            raise SystemExit("We close program, to safe your RAM memory from overflowing.")
        # Setting text of data on next day.
        self.timestamp.set_text(f"Day: {self.time.isoformat()}")
        # Return values required for generate an animation.
        return plots + lines + [self.timestamp]


nasaids = [1, 2, 3, 4]  # ID numbers in NASA database.
names = ["Mercury", "Venus", "Earth", "Mars"]
colors = ["gray", "orange", "green", "chocolate"]
sizes = [0.38, 0.95, 1.0, 0.53]
texty = [0.47, 0.73, 1, 1.5]
planet_datas = get_horizon_data(nasaids, names, colors, sizes)

# Creating object "ax", which will be a "window" to display an animation.
plt.style.use("dark_background")
fig = plt.figure(planet_datas["info"], figsize=[8, 8])
ax = plt.axes([0.0, 0.0, 1.0, 1.0], xlim=(-1.8, 1.8), ylim=(-1.8, 1.8))

CosmicObject("Sun", 28, "yellow", [0, 0, 0], [0, 0, 0])
system = SolarSystem()
system.time = datetime.strptime(planet_datas["date"], "%Y-%m-%d").date()

# Generating data for animation.
for nasaid in nasaids:
    planet = planet_datas[nasaid]
    # Adding planet to solar system.
    system.add_planet(
        CosmicObject(
            planet["name"],
            planet["size"] * 20,
            planet["color"],
            planet["r"],
            planet["v"],
        )
    )
    # Adding planet name to the animation window.
    ax.text(
        0,
        -(texty[nasaid - 1] + 0.1),
        planet["name"],
        color=planet["color"],
        zorder=1000,
        ha="center",
        fontsize="large",
    )


def animate(i):
    return system.evolve()


solar_animation = animation.FuncAnimation(
    fig,
    animate,
    repeat=False,
    frames=365,
    blit=True,
    interval=10
)
# Displaying the window.
plt.show()
