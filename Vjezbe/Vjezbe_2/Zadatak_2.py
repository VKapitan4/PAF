import numpy as np
import matplotlib.pyplot as plt

def fun(v_0,kut):
    t=[]
    x=[]
    y=[]
    v_x=[]
    v_y=[]
    a_x=0
    a_y=-9.81
    x_0=0
    y_0=0
    delta_t = 10
    N=10000
    for i in range(0,N):
        t.append((delta_t/N)*i)
    for i in t:
        v_x.append(v_0*np.cos(kut*(2*np.pi/360)) + a_x * i)
        v_y.append(v_0*np.sin(kut*(2*np.pi/360)) + a_y * i)

        x.append(x_0 + v_x[t.index(i)] * i)
        y.append(y_0 + v_y[t.index(i)] * i)
    
    plt.figure(figsize=(10,7))

    plt.subplot(2,2,1)
    plt.plot(x,y)
    plt.xlabel("$x(m)$")
    plt.ylabel("$y(m)$")

    plt.subplot(2,2,2)
    plt.plot(t,x)
    plt.xlabel("$t(s)$")
    plt.ylabel("$x(m)$")

    plt.subplot(2,2,3)
    plt.plot(t,y)
    plt.xlabel("$t(s)$")
    plt.ylabel("$y(m)$")

    plt.tight_layout()
    plt.show()

fun(100,40)