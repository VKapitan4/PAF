import numpy as np
import matplotlib.pyplot as plt
import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(10, 5, [0,0,0], [0,0,5], [0,0,0], [5,10,5], 0.01, 100)
p1.plot_trajectory('r')