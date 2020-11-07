import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

ejectVel = 10000000
ismDensity = 1.67E-25

t = np.linspace(0, 2 * np.pi, 100)

def radius(i):
    if i <= 1000:
        r = i
    elif 1000 < i <= 10000:
        r = 1000 + (i - 1000) ** 0.4
    elif 10000 < i <= 250000:
        r = 1010 + (i - 10000) ** 0.3
    else:
        r = 1051.6 + (i - 250000) ** 0.25
    return r

def supernova(i):
    x = radius(i) * np.cos(t)
    y = radius(i) * np.sin(t)
    plt.plot(x, y)
    plt.title('Supernova: A Super Nova Thing!')

super_plot = interactive(supernova,i=(0,750000,1))
super_plot


