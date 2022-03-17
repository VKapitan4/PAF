import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(2, 30, 0, 0)
print(p1.range())
p1.plot_trajectory()
p1.reset()
p1.set_initial_conditions(5, 30, 30, 50)
print(p1.range())
p1.plot_trajectory()