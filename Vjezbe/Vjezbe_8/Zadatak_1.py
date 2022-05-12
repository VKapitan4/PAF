import numpy as np
import matplotlib.pyplot as plt
import projectile as pro

p1 = pro.Projectile()
p1.set_initial_conditions(5, 45, 0, 0, 5, 0.001, 10, 0, 0.01)
p1.plot_trajectory('r')
p1.reset()
p1.set_initial_conditions(5, 45, 0, 0, 5, 0.001, 10, 0, 0.01)
print("domet Runge-kutta:")
p1.range('r')
p1.reset()
p1.set_initial_conditions(5, 45, 0, 0, 5, 0.001, 10, 0, 0.01)
p1.plot_trajectory()
p1.reset()
p1.set_initial_conditions(5, 45, 0, 0, 5, 0.001, 10, 0, 0.01)
print("domet Euler:")
p1.range()
p1.reset()