import harmonic_oscillator as ho
import matplotlib.pyplot as plt
import numpy as np

osc1 = ho.HarmonicOscillator()
osc2 = ho.HarmonicOscillator()

osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
osc1.plot_trajectory()

osc1.reset()
osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
period = osc1.period()
print(period)

osc1.reset()
osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.3)
t1, x1, v1, a1 = osc1.oscillator_data()

osc2.set_initial_conditions(5, 2, 10, 5, 60, 0.6)
t2, x2, v2, a2 = osc2.oscillator_data()

def fun(t):
    return 5*np.cos(np.sqrt(5/10)*t)+(2/np.sqrt(5/10))*np.sin(np.sqrt(5/10)*t)

x_analiticki = []
for i in t1:
    x_analiticki.append(fun(i))

plt.figure(figsize=(12,3))
plt.plot(t1, x_analiticki, zorder=0, color='blue')
plt.scatter(t1, x1, s=5, color='red')
plt.scatter(t2, x2, s=5, color='orange')
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")
plt.tight_layout()
plt.show()