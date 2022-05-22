import numpy as np
import matplotlib.pyplot as plt
import projectile as pro

p1 = pro.Projectile()
print(p1.angle_to_hit(10, 0, 0, 5, 1.5, "kocka", 2, 0.5, 0.01, 0.1, 1, 1))
x1 = []
y1 = []
for i in p1.r:
    x1.append(i[0])
    y1.append(i[1])

p2 = pro.Projectile()
print(p2.angle_to_hit(10, 0, 0, 5, 1.5, "kocka", 2, 0.5, 0.01, 0.05, 1.5, 0.5))
x2 = []
y2 = []
for i in p2.r:
    x2.append(i[0])
    y2.append(i[1])

fig, ax = plt.subplots()
plt.plot(x1, y1)
plt.scatter(p1.x_meta, p1.y_meta, marker='x', c="red", s=70)
circle = plt.Circle((p1.x_meta, p1.y_meta), p1.r_meta, fill=False)
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='box')
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()

fig, ax = plt.subplots()
plt.plot(x2, y2)
plt.scatter(p2.x_meta, p2.y_meta, marker='x', c="red", s=70)
circle = plt.Circle((p2.x_meta, p2.y_meta), p2.r_meta, fill=False)
ax.add_patch(circle)
ax.set_aspect('equal', adjustable='box')
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()