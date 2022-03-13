import numpy as np
import matplotlib.pyplot as plt

def fun(v_0,kut):
    t=[]
    x=[]
    y=[]
    x_0=0
    y_0=0
    delta_t = 10
    N=10000
    for i in range(0,N):
        t.append((delta_t/N)*i)
    for i in t:
        x.append(x_0+v_0*np.cos(kut*(2*np.pi/360))*i)
        y.append(y_0+v_0*np.sin(kut*(2*np.pi/360))*i)
    #fig = plt.figure()
    #ax = fig.add_subplot(131)
    plt.plot(x,y)
    plt.plot(t,x)
    plt.plot(t,y)
    #ax.set_aspect('equal')
    plt.show()

fun(2,40)