import numpy as np
import matplotlib.pyplot as plt
import projectile as pro

p1 = pro.Projectile()
p1.set_initial_conditions(10, 45, 0, 0, 5, 1.5, 0.5, 10, 0.01)
p1.range('r')
print("domet Runge-kutta:")
print(p1.x[-1])
x_runge = p1.x
y_runge = p1.y
p1.reset()

p1.set_initial_conditions(10, 45, 0, 0, 5, 1.5, 0.5, 10, 0.01)
p1.range()
print("domet Euler:")
print(p1.x[-1])
x_euler = p1.x
y_euler = p1.y
p1.reset()

plt.plot(x_runge, y_runge, label="Runge-Kutta")
plt.plot(x_euler, y_euler, label="Euler")
plt.legend(framealpha=1, frameon=True)
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()