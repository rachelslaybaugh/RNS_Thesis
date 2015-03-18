from matplotlib import pyplot as plt
import numpy as np
from matplotlib.pyplot import show

cores1 = [40800, 112200]
cores2 = [40800, 198528]
timeActual1 = [801.06, 330.51]
timeActual2 = [801.06, 142.62]
timeLinear1 = [801.06, 291.30]
timeLinear2 = [801.06, 164.63]

fig = plt.figure()
plt.plot(cores1, timeActual1, 'ko-', linewidth=1.5, markersize=10)
plt.plot(cores1, timeLinear1, 'k*:', linewidth=3, markersize=12) 
leg = plt.legend(("measured", "linear"), loc="lower left")
plt.plot(cores2, timeActual2, 'ko-', linewidth=1.5, markersize=10)
plt.plot(cores2, timeLinear2, 'k*:', linewidth=3, markersize=12) 
plt.title("PWR Strong Scaling, Preconditioned RQI", fontsize=20)
plt.ylabel("Solver Time (m)", fontsize=18)
plt.xlabel("Cores", fontsize=18)
plt.grid(True)
#plt.xlim([100000,200000])
#plt.xticks([4e4, 8e4, 12e5, 16e5, 2e6])
#plt.ylim([100, 900])
#plt.yticks([25, 30, 35, 40, 45, 50])

show()

