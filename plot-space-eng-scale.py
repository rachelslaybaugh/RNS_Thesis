from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import show

coresB = [110880, 198528]
timeB = [53.61, 34.991]
timeBlinear = [53.61, 29.94]

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
ax.plot(coresB, timeB, 'ko-')
ax.plot(coresB, timeBlinear, 'ko:') 
ax.set_title("PWR Strong Scaling, Doubling Spatial Blocks", fontsize=20)
ax.set_ylabel("Wall Time (m)", fontsize=16)
ax.set_xlabel("Cores", fontsize=16)
leg = ax.legend(("measured", "linear"), loc="lower left")
ax.grid(True)
ax.set_xlim([100000,200000])
ax.set_xticks([100000, 125000, 150000, 175000, 200000])
ax.set_ylim([20, 55])
ax.set_yticks([25, 30, 35, 40, 45, 50])

coresE = [112200, 198528]
timeEorig = [49.61, 34.991]
timeEnew = [38.33, 34.99]
timeElinearOrig = [49.61, 28.04]
timeElinearNew = [38.33, 21.66]

ax = fig.add_subplot(2,1,2, sharex=ax)
ax.plot(coresE, timeEorig, 'ko-')
ax.plot(coresE, timeElinearOrig, 'ko:') 
ax.plot(coresE, timeEnew, 'g*-')
ax.plot(coresE, timeElinearNew, 'g*:') 
ax.set_title("PWR Strong Scaling, Doubling Energy Sets")
ax.set_ylabel("Wall Time (m)")
ax.set_xlabel("Cores")
leg = ax.legend(("measured, orig", "linear, orig", "measured, new", "linear, new"), loc="lower left")
ax.grid(True)
ax.set_xlim([100000,200000])
ax.set_xticks([100000, 125000, 150000, 175000, 200000])
ax.set_ylim([20, 55])
ax.set_yticks([25, 30, 35, 40, 45, 50])
show()

