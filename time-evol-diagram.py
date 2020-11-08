import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

lightSpeed = 3 * 10**8
ejectVel = lightSpeed / np.sqrt(50)
ismDensity = 1.66 * 10**-20
heatRatio = 1.625

sedovTaylor = ((0.75 / 16) * (lightSpeed**2 / (np.pi * heatRatio * ismDensity))) ** 0.2
snowPlow = 1.62 * 10 ** 7
pDrive = 87089.51
sunMass = 1.989 * 10**30

m = 1.4

fig = plt.figure()
ax = plt.axes(xlim=(-90000, 90000), ylim=(-90000, 90000))
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,


def update(i):
    t = np.linspace(0, 2 * np.pi, 100)
    if i <= 50:
        r = 20 * i
    elif 50 < i <= 5050:
        rInit = 1000
        r = rInit + 10 * (i - 50)
    elif 5050 < i <= 15050:
        rInit = 51000
        r = rInit + 3 * (i - 5050)
    else:
        rInit = 81000
        r = rInit + (i - 15050)
    x = r * np.cos(t)
    y = r * np.sin(t)
    line.set_data(x, y)
    return line,


ani = animation.FuncAnimation(fig, update, init_func=init, frames=20000, interval=1, blit=True)
plt.show()
