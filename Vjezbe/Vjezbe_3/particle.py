import numpy as np

class Particle:
    def __init__(self):
        t=[]
        ax=0
        ay=-9.81
        vx=[v_0*np.cos(kut)]
        vy=[v_0*np.sin(kut)]
        x=[x_0]
        y=[y_0]
        raspon_t = 10
        N=10000
        delta_t = raspon_t/N
        for i in range(0,N):
            t.append(delta_t*i)

    def set_initial_conditions(self, v_0, kut, x_0, y_0):
        self.v_0 = v_0
        self.kut = kut
        self.x_0 = x_0
        self.y_0 = y_0

    def reset(self):
        del(self.v_0)
        del(self.kut)
        del(self.x_0)
        del(self.y_0)

    def __move(self):
        vx.append(v_x[-1]+ax*delta_t)
        vy.append(v_y[-1]+ay*delta_t)
        x.append(x[-1]+vx[-1]*delta_t)
        y.append(y[-1]+vy[-1]*delta_t)

    def range(self):
        while 

    def printInfo(self):
        print(f"opcetna brzina: {self.v_0}, kut: {self.kut} pocetni polozaj: {self.x_0}")