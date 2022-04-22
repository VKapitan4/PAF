import projectile as pro
import matplotlib.pyplot as plt

avion1 = pro.ProjectileDrop(2000, 200)
x, y, vx, vy, t = avion1.projektil(0.01)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
plt.plot(x,y)
plt.xlabel("$x(m)$")
plt.ylabel("$y(m)$")

plt.subplot(1,2,2)
plt.plot(t,vy)
plt.xlabel("$t(s)$")
plt.ylabel("$vy(m/s)$")

plt.tight_layout()
plt.show()

