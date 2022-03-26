import particle as prt
import matplotlib.pyplot as plt

p = prt.Particle()
a = p.angle_to_hit_target(80, 20, 20, 5)
print(a)

p.reset()
#p.set_initial_conditions(80, 35.87, 0, 0, 0.001)
#p.plot_trajectory()