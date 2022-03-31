import harmonic_oscillator as ho

osc1 = ho.HarmonicOscillator()
osc1.set_initial_conditions(0, 0, 10, 5, 10, 0.01)
osc1.plot_trajectory()