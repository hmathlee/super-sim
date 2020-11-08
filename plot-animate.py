import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

lightSpeed = 3 * 10**8
ejectVel = lightSpeed / np.sqrt(50)
ismDensity = 1.66 * 10**-20
heatRatio = 2.5832323

sedovTaylor = (0.75 // 16) * (lightSpeed**2 // (np.pi * heatRatio * ismDensity))
snowPlow = 1.62 * 10 ** 7
pDrive = 87089.51
sunMass = 1.989 * 10**30

t = np.linspace(0, 2 * np.pi, 100)


def radius(i, m):
    r = 0
    if i <= 1000:
        r = i
    elif 1000 < i <= 10000:
        rInit = r
        r = rInit + sunMass * m * sedovTaylor * (i - 1000) ** 0.4
    elif 10000 < i <= 250000:
        rInit = r
        r = rInit + sunMass * m * snowPlow * (i - 10000) ** 0.3
    else:
        rInit = r
        r = rInit + pDrive * (i - 250000) ** 0.25
    return r


def supernova(time, mass):
    x = radius(time, mass) * np.cos(t)
    y = radius(time, mass) * np.sin(t)
    plt.plot(x, y)
    plt.title('Supernova: A Super Nova Thing!')


superPlot = interactive(supernova, time=(0, 750000, 1), mass=(1.4, 200, 0.1))
superPlot


