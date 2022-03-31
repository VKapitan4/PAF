import harmonic_oscillator as ho

osc1 = ho.HarmonicOscillator()
osc1.set_initial_conditions(5, 2, 10, 5, 60, 0.1)
osc1.plot_trajectory()