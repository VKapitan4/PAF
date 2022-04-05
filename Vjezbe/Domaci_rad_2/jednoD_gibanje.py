import matplotlib.pyplot as plt
import numpy as np

class Jednodimenzionalno_gibanje:
    def __init__(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]
        self.t=[0]

    def set_initial_conditions(self, x_0, v_0, F, m, vrijeme, dt):
        self.F.append(F(x_0,v_0,0))
        self.a.append(self.F[0]/m)
        self.v.append(v_0)
        self.x.append(x_0)
        self.F_fun=F
        self.m=m
        self.vrijeme=vrijeme
        self.dt=dt
        self.N = int(np.floor(vrijeme/dt))

    def reset(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]
        self.t=[0]

    def __move(self):
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1]+self.v[-1]*self.dt)
        self.F.append(self.F_fun(self.x[-1],self.v[-1],self.t[-1]))
        self.a.append(self.F[-1]/self.m)

    def motion_data(self):
        self.t.pop(0)
        for i in range(1,self.N+1):
            self.t.append(i*self.dt)
            self.__move()
        self.t.insert(0,0)
        return self.t, self.x, self.v, self.a