import particle as prt

p1 = prt.Particle()

p1.set_initial_conditions(100, 80, 0, 0, 0.001)
print(p1.range())
p1.reset()
p1.set_initial_conditions(100, 80, 0, 0, 0.001)
p1.plot_trajectory()

#import matplotlib.pyplot as plt

#print(type(plt.Circle))