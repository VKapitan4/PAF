import numpy as np
import matplotlib.pyplot as plt

def fun(F,m):
    t=[]
    x=[]
    v=[]
    a=[]
    delta_t = 10
    v_0=5
    x_0=10
    N=10000
    for i in range(0,N):
        t.append((delta_t/N)*i)
    for i in t:
        a.append(F/m)
        v.append(v_0+a[t.index(i)]*i)
        x.append(x_0+v[t.index(i)]*i)

    plt.figure(figsize=(10,7))

    plt.subplot(2,2,1)
    plt.plot(t,a)
    plt.xlabel("$t(s)$")
    plt.ylabel("$a(m/s^2)$")

    plt.subplot(2,2,2)
    plt.plot(t,v)
    plt.xlabel("$t(s)$")
    plt.ylabel("$v(m/s)$")

    plt.subplot(2,2,3)
    plt.plot(t,x)
    plt.xlabel("$t(s)$")
    plt.ylabel("$x(m)$")
    
    plt.tight_layout()
    plt.show()

fun(10,10)
    