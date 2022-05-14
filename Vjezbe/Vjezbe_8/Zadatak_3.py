import numpy as np
import matplotlib.pyplot as plt
import projectile as pro


p1 = pro.Projectile()

Cd = []
domet1 = []
dx = 0.02
for i in range(0, 101):
    Cd.append(i*dx)
    p1.set_initial_conditions(10, 45, 0, 0, 5, 1.5, 2, Cd[-1], 0.01)
    p1.range('r')
    domet1.append(p1.x[-1])
    p1.reset()

m = []
domet2 = []
dx = 0.1
for i in range(1, 501):
    m.append(i*dx)
    p1.set_initial_conditions(10, 45, 0, 0, m[-1], 1.5, 2, 1, 0.01)
    p1.range('r')
    domet2.append(p1.x[-1])
    p1.reset()

plt.plot(Cd, domet1)
plt.xlabel("$Cd()$")
plt.ylabel("$domet(m)$")
plt.show()

plt.plot(m, domet2)
plt.xlabel("$m(kg)$")
plt.ylabel("$domet(m)$")
plt.show()    