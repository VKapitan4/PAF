import numpy as np
import matplotlib.pyplot as plt
import universe
import planet

planet1 = planet.Planet()
planet1.set_initial_conditions(1, [0,0], [0,5000])

planet2 = planet.Planet()
planet2.set_initial_conditions(2, [10,0], [0,0])

planeti = [planet1, planet2]

svemir = universe.Universe(planeti)
svemir.plot_trajectory(0.01, 10)
