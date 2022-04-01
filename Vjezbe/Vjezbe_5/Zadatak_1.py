import harmonic_oscillator as ho
import matplotlib.pyplot as plt

osc1 = ho.HarmonicOscillator()
osc2 = ho.HarmonicOscillator()

osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
osc1.plot_trajectory()

osc1.reset()
osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
period = osc1.period()
print(period)

osc1.reset()
osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
t1, x1, v1, a1 = osc1.oscillator_data()

osc2.set_initial_conditions(5, 2, 10, 5, 60, 0.3)
t2, x2, v2, a2 = osc2.oscillator_data()

#def fun(t):
#    return

plt.figure(figsize=(12,3))
plt.scatter(t1, x1, s=5)
plt.scatter(t2, x2, s=5)
plt.pot()
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")
plt.tight_layout()
plt.show()