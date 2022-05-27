import numpy as np
import matplotlib.pyplot as plt
import particle as prt

def E(t):
    return np.array([0,0,0])

def B(t):
    return np.array([0,0,t/10])

def B_const(t):
    return np.array([0,0,0.5])

p1 = prt.Particle()
p1.set_initial_conditions(1, 5, E(0), B(0), [0,0,0], [0.1,0.1,0.1], 0.01, 10)
p1.evolve(E, B, 'r')
x1 = p1.x
y1 = p1.y
z1 = p1.z
p1.reset()

p1.set_initial_conditions(1, 5, E(0), B(0), [0,0,0], [0.1,0.1,0.1], 0.01, 10)
p1.evolve(E, B_const, 'r')
x2 = p1.x
y2 = p1.y
z2 = p1.z
p1.reset()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(x1, y1, z1, label='vremenski ovisno polje')
ax.plot(x2, y2, z2, label='polje konstantno u vremenu')
ax.set_xlabel('$x(m)$')
ax.set_ylabel('$y(m)$')
ax.set_zlabel('$z(m)$')
plt.legend(framealpha=1, frameon=True)
plt.show()

p1 = prt.Particle()
p1.set_initial_conditions(1, 5, E(0), B(0), [0,0,0], [0.1,0.1,0.1], 0.01, 10)
p1.evolve(E, B, 'r')
x1 = p1.x
y1 = p1.y
z1 = p1.z
p1.reset()

p1.set_initial_conditions(1, -5, E(0), B(0), [0,0,0], [0.1,0.1,0.1], 0.01, 10)
p1.evolve(E, B, 'r')
x2 = p1.x
y2 = p1.y
z2 = p1.z
p1.reset()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
plt.title('promjenjivo magnetsko polje')
ax.plot(x1, y1, z1, label='elektron')
ax.plot(x2, y2, z2, label='pozitron')
ax.set_xlabel('$x(m)$')
ax.set_ylabel('$y(m)$')
ax.set_zlabel('$z(m)$')
plt.legend(framealpha=1, frameon=True)
plt.show()