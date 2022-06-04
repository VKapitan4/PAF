import numpy as np
import matplotlib.pyplot as plt
import universe

p1 = universe.Planet(1.989 * 10**(30), "Sunce") # Sunce
p2 = universe.Planet(3.285 * 10**(23), "Merkur")
p3 = universe.Planet(4.867 * 10**(24), "Venera")
p4 = universe.Planet(5.9742 * 10**(24), "Zemlja") # Zemlja
p5 = universe.Planet(6.39 * 10**(23), "Mars")

p1.set_initial_conditions([0,0], [0,0])
p2.set_initial_conditions([68.962 * 10**(9), 0], [0, 47870])
p3.set_initial_conditions([108.85 * 10**(9), 0], [0, 35020])
p4.set_initial_conditions([1.496 * 10**(11), 0], [0, 29783])
p5.set_initial_conditions([208.23 * 10**(9), 0], [0, 24077])

planeti = [p1, p2, p3, p4, p5]

svemir = universe.Universe(planeti)
svemir.animate_plot(10000, 5*365.242*24*60*60)