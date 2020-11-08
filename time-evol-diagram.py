# Time evolution diagram template. Intended to illustrate how supernova blast radius expands
#   at a rapidly decreasing rate. The supernova will transition between different phases, at
#   which the radius is proportional to different powers of time.

# Note: Time is NOT TO SCALE. Please see Jupyter Notebook in this repository for accurate
#   time scale.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Here, we examine the time evolution of a supernova blast radius of a 1.4 solar-mass star.
m = 1.4

# Create plot.
fig = plt.figure()
ax = plt.axes(xlim=(-90000, 90000), ylim=(-90000, 90000))
ax.set_title('Supernova Expansion Simulation')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax = plt.gca()
ax.set_facecolor('#000000')
line, = ax.plot([], [], lw=2)

# Initialize plot (i.e. get the animation running).
def init():
    line.set_data([], [])
    return line,

# Animate plot.
def update(i):
    t = np.linspace(0, 2 * np.pi, 100)
    if i <= 50:
        r = 20 * i
        line.set_color("red")
    elif 50 < i <= 5050:
        rInit = 1000
        r = rInit + 10 * (i - 50)
        line.set_color("green")
    elif 5050 < i <= 15050:
        rInit = 51000
        r = rInit + 3 * (i - 5050)
        line.set_color("blue")
    else:
        rInit = 81000
        r = rInit + (i - 15050)
        line.set_color("black")
    x = r * np.cos(t)
    y = r * np.sin(t)
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, update, init_func=init, frames=20000, interval=1, blit=True)
plt.show()