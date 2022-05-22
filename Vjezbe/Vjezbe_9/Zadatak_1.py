import numpy as np
import matplotlib.pyplot as plt
import bungee

skok1 = bungee.Bungee(60, 100, 1, 10, 40, 0.001)
skok1.plot_trajectory()
skok1.reset()
skok1.plot_energy()

skok2 = bungee.Bungee(60, 100, 0, 10, 40, 0.001)
skok2.plot_trajectory()
skok2.reset()
skok2.plot_energy()