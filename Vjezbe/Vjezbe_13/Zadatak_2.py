import numpy as np
import matplotlib.pyplot as plt
import universe

au = 1.496 * 10**(11)

p1 = universe.Planet(1.989 * 10**(30), "Sunce") # Sunce
p2 = universe.Planet(3.285 * 10**(23), "Merkur")
p3 = universe.Planet(4.867 * 10**(24), "Venera")
p4 = universe.Planet(5.9742 * 10**(24), "Zemlja") # Zemlja
p5 = universe.Planet(6.39 * 10**(23), "Mars")
komet = universe.Planet(10**(14), "komet")

p1.set_initial_conditions([0,0], [0,0])
p2.set_initial_conditions([68.962 * 10**(9), 0], [0, 47870])
p3.set_initial_conditions([108.85 * 10**(9), 0], [0, 35020])
p4.set_initial_conditions([1.496 * 10**(11), 0], [0, 29783])
p5.set_initial_conditions([208.23 * 10**(9), 0], [0, 24077])
komet.set_initial_conditions([-4.5*au, 0], [25000, 5000])

planeti = [p1, p2, p3, p4, p5, komet]

svemir = universe.Universe(planeti)
polozaji, brzine = svemir.generate_init_for_collision(15000)

for i in planeti:
    i.reset()

p1 = universe.Planet(1.989 * 10**(30), "Sunce") # Sunce
p2 = universe.Planet(3.285 * 10**(23), "Merkur")
p3 = universe.Planet(4.867 * 10**(24), "Venera")
p4 = universe.Planet(5.9742 * 10**(24), "Zemlja") # Zemlja
p5 = universe.Planet(6.39 * 10**(23), "Mars")
komet = universe.Planet(10**(14), "komet")

p1.set_initial_conditions(polozaji[0], brzine[0])
p2.set_initial_conditions(polozaji[1], brzine[1])
p3.set_initial_conditions(polozaji[2], brzine[2])
p4.set_initial_conditions(polozaji[3], brzine[3])
p5.set_initial_conditions(polozaji[4], brzine[4])
komet.set_initial_conditions(polozaji[5], brzine[5])

planeti = [p1, p2, p3, p4, p5, komet]

svemir = universe.Universe(planeti)
svemir.animate_plot(150000, 1*290*24*60*60, 1, True)