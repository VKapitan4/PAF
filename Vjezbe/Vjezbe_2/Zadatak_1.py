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
    plt.plot(t,a)
    plt.show()
    plt.plot(t,v)
    plt.show()
    plt.plot(t,x)
    plt.show()

fun(10,10)
    