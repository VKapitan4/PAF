import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    def __init__(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]

    def set_initial_conditions(self, x_0, v_0, m, k, vrijeme, dt):
        self.F.append(-k*x_0)
        self.a.append(self.F[0]/m)
        self.v.append(v_0)
        self.x.append(x_0)
        self.m=m
        self.k=k
        self.dt=dt
        self.t=[]
        N = int(np.floor(vrijeme/dt))+1
        for i in range(0,N):
            self.t.append(i*dt)

    def reset(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]

    def __move(self):
        self.F.append(-self.k*self.x[-1])
        self.a.append(self.F[-1]/self.m)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1]+self.x[-1]*self.dt)

    def plot_trajectory(self):
        for i in self.t:
            self.__move()
        plt.plot(self.t, self.x)
        plt.xlabel("$t(m)$")
        plt.ylabel("$x(m)$")
        plt.show()