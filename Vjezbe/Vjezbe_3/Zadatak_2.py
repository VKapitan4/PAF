import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()
analiticki_domet = 8.827986
relativna_pogreska = []

for i in np.arange(0.001, 0.1, 0.001):
    p1.reset()
    p1.set_initial_conditions(10,60,0,0,i)
    numericki_domet = p1.range()
    relativna_pogreska.append(100*abs(numericki_domet - analiticki_domet)/analiticki_domet)

plt.plot(np.arange(0.001, 0.1, 0.001), relativna_pogreska)
plt.xlabel("dt(s)")
plt.ylabel("apsoluna relativna pogreska (%)")
plt.show()