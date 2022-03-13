import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(m,delta_t,v_0,kut_v_0,F,kut_F):
    N=delta_t*1000
    x_0=0
    y_0=0
    v_x=[]
    v_y=[]
    x=[]
    y=[]
    t=[]

    for i in range(0,N):
        t.append((delta_t/N)*i)
    
    for i in t:
        a_x = F*np.cos(kut_F*(2*np.pi/360))
        a_y = F*np.sin(kut_F*(2*np.pi/360))

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * i)
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * i)

        x.append(x_0 + v_x[t.index(i)] * i)
        y.append(y_0 + v_y[t.index(i)] * i)

    plt.plot(x,y)
    plt.plot(t,x)
    plt.plot(t,y)
    plt.show()

def kosi_hitac(m,delta_t,v_0,kut_v_0):
    N=delta_t*1000
    x_0=0
    y_0=0
    v_x=[]
    v_y=[]
    x=[]
    y=[]
    t=[]

    for i in range(0,N):
        t.append((delta_t/N)*i)

    for i in t:
        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * i)
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * i)

        x.append(x_0 + v_x[t.index(i)] * i)
        y.append(y_0 + v_y[t.index(i)] * i)

    plt.plot(x,y)
    plt.plot(t,x)
    plt.plot(t,y)
    plt.show()