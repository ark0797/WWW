import numpy as np
import pylab
import matplotlib as plt

tmin = -20.0
tmax = 20.0

dt = 0.01
tlist = np.arange (tmin, tmax, dt)

pylab.ion()

for n in range (50):
        xlist = [np.sin(t + n) for t in tlist]
        ylist = [np.cos(2 * t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()
