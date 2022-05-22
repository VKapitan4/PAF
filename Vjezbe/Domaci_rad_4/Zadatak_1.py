import numpy as np
import matplotlib.pyplot as plt
import projectile as pro

p1 = pro.Projectile()
p1.set_initial_conditions(10, 45, 0, 0, 5, 1.5, "kocka", 0.39894, 10, 0.01)
p1.range('r')
print("domet kocke:")
print(p1.x[-1])
x_kocka = p1.x
y_kocka = p1.y
p1.reset()

p2 = pro.Projectile()
p2.set_initial_conditions(10, 45, 0, 0, 5, 1.5, "kugla", 0.39894, 10, 0.01)
p2.range('r')
print("domet kugle:")
print(p2.x[-1])
x_kugla = p2.x
y_kugla = p2.y
p2.reset()

plt.plot(x_kocka, y_kocka, label="kocka")
plt.plot(x_kugla, y_kugla, label="kugla")
plt.legend(framealpha=1, frameon=True);
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")
plt.show()