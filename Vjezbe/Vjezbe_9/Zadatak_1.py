import numpy as np
import matplotlib.pyplot as plt
import bungee

skok1 = bungee.Bungee(60, 100, 1, 10, 40, 0.01)
skok1.plot_trajectory()
skok1.plot_energy()
print(skok1.E[0])