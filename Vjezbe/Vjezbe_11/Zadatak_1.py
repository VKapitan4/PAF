import numpy as np
import matplotlib.pyplot as plt
import universe  #triba prominit ime

p1 = universe.Planet(1.989 * 10**(30), "Sunce") # Sunce
p2 = universe.Planet(5.9742 * 10**(24), "Zemlja") # Zemlja

p1.set_initial_conditions([0,0], [0,0])
p2.set_initial_conditions([1.496 * 10**(11), 0], [0, 29783])

planeti = [p1, p2]

svemir = universe.Universe(planeti)
svemir.evolve(1000, 365.242*24*60*60)