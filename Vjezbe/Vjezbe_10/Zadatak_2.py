import numpy as np
import matplotlib.pyplot as plt
import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(1, 1, [0,0,0], [0,0,1], [0,0,0], [0.1,0.1,0.1], 0.01, 25)
p1.evolve('r')
x1 = p1.x
y1 = p1.y
z1 = p1.z
p1.reset()

p1.set_initial_conditions(1, 1, [0,0,0], [0,0,1], [0,0,0], [0.1,0.1,0.1], 0.01, 25)
p1.evolve()
x2 = p1.x
y2 = p1.y
z2 = p1.z
p1.reset()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x1, y1, z1, label='Runge-Kutta')
ax.plot(x2, y2, z2, label='Euler')
ax.set_xlabel('$x(m)$')
ax.set_ylabel('$y(m)$')
ax.set_zlabel('$z(m)$')
plt.legend(framealpha=1, frameon=True)
plt.show()