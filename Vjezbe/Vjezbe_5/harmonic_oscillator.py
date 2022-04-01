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
        self.vrijeme=vrijeme
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

        plt.figure(figsize=(10,7))

        plt.subplot(3,1,1)
        plt.scatter(self.t, self.x, s=2)
        plt.xlabel("$t(s)$")
        plt.ylabel("$x(m)$")

        plt.subplot(3,1,2)
        plt.scatter(self.t, self.v, s=2)
        plt.xlabel("$t(s)$")
        plt.ylabel("$v(m)$")

        plt.subplot(3,1,3)
        plt.scatter(self.t, self.a, s=2)
        plt.xlabel("$t(s)$")
        plt.ylabel("$a(m)$")

        plt.tight_layout()
        plt.show()

    def oscillator_data(self):
        self.t.pop(0)
        for i in self.t:
            self.__move()
        self.t.insert(0,0)

        return self.t, self.x, self.v, self.a

    def period(self):
        t1=[0]
        i=1
        while (self.x[-1]<self.x[0] and self.x[-2]<self.x[0]) or (self.x[-1]>self.x[0] and self.x[-2]>self.x[0]) or len(self.x)==1 or len(self.x)==2:
            t1.append(i*self.dt)
            self.__move()
            i=i+1
        x1=self.x[-1]
        t2=[0]
        i=1
        duljina_x = len(self.x)
        while (self.x[-1]<self.x[0] and self.x[-2]<self.x[0]) or (self.x[-1]>self.x[0] and self.x[-2]>self.x[0]) or len(self.x)==duljina_x or len(self.x)==duljina_x+1:
            t2.append(i*self.dt)
            self.__move()
            i=i+1
        return t1[-1]+t2[-1]
