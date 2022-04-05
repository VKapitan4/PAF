import jednoD_gibanje
import matplotlib.pyplot as plt

def fun_1(x,v,t):
    return -20*x

oscilator = jednoD_gibanje.Jednodimenzionalno_gibanje()
oscilator.set_initial_conditions(3, 4, fun_1, 5, 10, 0.05)
t1, x1, v1, a1 = oscilator.motion_data()

plt.figure(figsize=(10,7))
plt.suptitle('Harmonički oscilator')

plt.subplot(3,1,1)
plt.scatter(t1, x1, s=5, color='blue')
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")

plt.subplot(3,1,2)
plt.scatter(t1, v1, s=5, color='red')
plt.xlabel("$t(s)$")
plt.ylabel("$v(m)$")

plt.subplot(3,1,3)
plt.scatter(t1, a1, s=5, color='orange')
plt.xlabel("$t(s)$")
plt.ylabel("$a(m)$")

plt.tight_layout()
plt.show()


def fun_2(x,v,t):
    return 5

jednoliko_ubrzano = jednoD_gibanje.Jednodimenzionalno_gibanje()
jednoliko_ubrzano.set_initial_conditions(2, 1, fun_2, 10, 5, 0.05)
t2, x2, v2, a2 = jednoliko_ubrzano.motion_data()

plt.figure(figsize=(10,7))
plt.suptitle('Gibanje pod konstantnom silom')

plt.subplot(2,2,1)
plt.scatter(t2, x2, s=5, color='blue')
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")

plt.subplot(2,2,2)
plt.scatter(t2, v2, s=5, color='red')
plt.xlabel("$t(s)$")
plt.ylabel("$v(m)$")

plt.subplot(2,2,3)
plt.scatter(t2, a2, s=5, color='orange')
plt.xlabel("$t(s)$")
plt.ylabel("$a(m)$")

plt.tight_layout()
plt.show()