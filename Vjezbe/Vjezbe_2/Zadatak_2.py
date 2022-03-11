import numpy as np
import matplotlib.pyplot as plt

def fun(v_0,kut):
    t=[]
    x=[]
    y=[]
    x_0=0
    y_0=0
    delta_t = 10
    for i in range(0,N):
        t.append((delta_t/N)*i)
    for i in t:
        x.append(x_0+v_0*np.cos(kut)*i)
        y.append(y_0+v-0*np.sin(kut)*i)