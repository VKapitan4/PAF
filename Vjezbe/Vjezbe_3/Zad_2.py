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

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.plot(np.arange(0, 90, 0.2), domet)
plt.xlabel("kut(stupnjevi)")
plt.ylabel("domet(m)")

plt.subplot(1,2,2)
plt.plot(np.arange(0, 90, 0.2), vrijeme)
plt.xlabel("kut(stupnjevi)")
plt.ylabel("t(s)")

plt.tight_layout()
plt.show()