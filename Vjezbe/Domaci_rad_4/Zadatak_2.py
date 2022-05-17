import numpy as np
import matplotlib.pyplot as plt
import projectile as pro

p1 = pro.Projectile()
p1.angle_to_hit(10, 0, 0, 5, 1.5, "kocka", 2, 0.5, 0.01, 0.1, 1, 1)

p2 = pro.Projectile()
p2.angle_to_hit(10, 0, 0, 5, 1.5, "kocka", 2, 0.5, 0.01, 0.05, 1.5, 0.5)

fig, ax = plt.subplots()
plt.plot(p1.x, p1.y)
plt.scatter(p1.x_meta, p1.y_meta, marker='x', c="red", s=70)
circle = plt.Circle((p1.x_meta, p1.y_meta), p1.r_meta, fill=False)
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='box')
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()

fig, ax = plt.subplots()
plt.plot(p2.x, p2.y)
plt.scatter(p2.x_meta, p2.y_meta, marker='x', c="red", s=70)
circle = plt.Circle((p2.x_meta, p2.y_meta), p2.r_meta, fill=False)
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='box')
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()