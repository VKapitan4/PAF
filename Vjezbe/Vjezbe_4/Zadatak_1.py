import calculus
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3

def g(x):
    return np.sin(x)

x1_1, d1_1 = calculus.derivacija_na_rasponu(f,1,2,dx=0.1,m=1)
x2_1, d2_1 = calculus.derivacija_na_rasponu(g,0,10,dx=0.2,m=1)

x1_2, d1_2 = calculus.derivacija_na_rasponu(f,1,2,dx=0.2,m=1)
x2_2, d2_2 = calculus.derivacija_na_rasponu(g,0,10,dx=0.4,m=1)

x1_a=np.arange(1,2,0.0001)
x2_a=np.arange(0,10,0.0001)

d1_a=[]
d2_a=[]
for i in x1_a:
    d1_a.append(3*i**2)
for i in x2_a:
    d2_a.append(np.cos(i))

plt.scatter(x1_1, d1_1, s=7, c='orange')
plt.scatter(x1_2, d1_2, s=7, c='red')
plt.plot(x1_a, d1_a)
plt.xlabel("$x$")
plt.ylabel("$f(x)$")
plt.show()

plt.scatter(x2_1, d2_1, s=7, c='orange')
plt.scatter(x2_2, d2_2, s=7, c='red')
plt.plot(x2_a, d2_a)
plt.xlabel("$x$")
plt.ylabel("$g(x)$")
plt.show()