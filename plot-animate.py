import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interactive

ejectVel = 10000000
ismDensity = 1.67E-25

t = np.linspace(0, 2 * np.pi, 100)
sedov_taylor_coeff = (0.75 // 16) * (9 * 10**16 // (np.pi * 2.5832323 * 1.66 * 10**-20))
snowplow_coeff = 1.62 * 10 ** 7
pdrive_coeff = 87089.51
sun_mass = 1.989 * 10**30

def radius(i, m):
    r = 0
    if i <= 1000:
        r = i
    elif 1000 < i <= 10000:
        r_0 = r
        r = r_0 + sun_mass * m * sedov_taylor_coeff * (i - 1000) ** 0.4
    elif 10000 < i <= 250000:
        r_0 = r
        r = r_0 + sun_mass * m * snowplow_coeff * (i - 10000) ** 0.3
    else:
        r_0 = r
        r = r_0 + pdrive_coeff * (i - 250000) ** 0.25
    return r

def supernova(time, mass):
    x = radius(time, mass) * np.cos(t)
    y = radius(time, mass) * np.sin(t)
    plt.plot(x, y)
    plt.title('Supernova: A Super Nova Thing!')

super_plot = interactive(supernova,time=(0,750000,1),mass=(1.4,200,0.1))
super_plot


