import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()

domet=[]
for i in np.arange(0, 90, 0.2):
    p1.reset()
    p1.set_initial_conditions(10, i, 0, 0, 0.001)
    domet.append(p1.range())

vrijeme=[]
for i in np.arange(0, 90, 0.2):
    p1.reset()
    p1.set_initial_conditions(10, i, 0, 0, 0.001)
    vrijeme.append(p1.total_time())

plt.plot(np.arange(0, 90, 0.2), domet)
plt.show()
plt.plot(np.arange(0, 90, 0.2), vrijeme)
plt.show()