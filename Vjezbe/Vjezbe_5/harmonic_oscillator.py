import matplotlib.pyplot as plt
import numpy as np

class HarmonicOscillator:
    def __init__(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]
        self.t=[0]

    def set_initial_conditions(self, x_0, v_0, m, k, vrijeme, dt):
        self.F.append(-k*x_0)
        self.a.append(self.F[0]/m)
        self.v.append(v_0)
        self.x.append(x_0)
        self.m=m
        self.k=k
        self.dt=dt
        N = int(np.floor(vrijeme/dt))
        for i in range(1,N+1):
            self.t.append(i*dt)

    def reset(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.x=[]
        self.t=[0]

    def __move(self):
        self.F.append(-self.k*self.x[-1])
        self.a.append(self.F[-1]/self.m)
        self.v.append(self.v[-1]+self.a[-1]*self.dt)
        self.x.append(self.x[-1]+self.v[-1]*self.dt)

    def plot_trajectory(self):
        self.t.pop(0)
        for i in self.t:
            self.__move()
        self.t.insert(0,0)
        plt.scatter(self.t, self.x, s=5)
        plt.xlabel("$t(m)$")
        plt.ylabel("$x(m)$")
        plt.show()