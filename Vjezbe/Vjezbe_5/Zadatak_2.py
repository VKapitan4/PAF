import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import numpy as np

koraci=[]
periodi_an=[]
periodi_num=[]
for i in np.arange(0.01, 0.6, 0.01):
    koraci.append(i)
    periodi_an.append((2*np.pi)/np.sqrt(5/10))
    a = ho.HarmonicOscillator()
    a.set_initial_conditions(5, 2, 10, 5, 60, i)
    periodi_num.append(a.period())
    a.reset()

plt.figure(figsize=(12,3))
plt.plot(koraci, periodi_an, zorder=0, color='blue')
plt.plot(koraci, periodi_num, color='orange')
plt.xlabel("$dt(s)$")
plt.ylabel("$T(s)$")
plt.tight_layout()
plt.show()