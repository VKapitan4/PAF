import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.ax=0
        self.ay=-9.81
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.delta_t = 0.001

    def set_initial_conditions(self, v_0, kut, x_0, y_0):
        self.vx.append(v_0*np.cos((kut/360)*2*np.pi))
        self.vy.append(v_0*np.sin((kut/360)*2*np.pi))
        self.x.append(x_0)
        self.y.append(y_0)

    def reset(self):
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]

    def __move(self):
        self.vx.append(self.vx[-1]+self.ax*self.delta_t)
        self.vy.append(self.vy[-1]+self.ay*self.delta_t)
        self.x.append(self.x[-1]+self.vx[-1]*self.delta_t)
        self.y.append(self.y[-1]+self.vy[-1]*self.delta_t)

    def range(self):
        while self.y[-1]>self.y[0] or len(self.y)==1:
            self.__move()
        domet = self.x[-1] - self.x[0]
        return domet
    
    def plot_trajectory(self):
        while self.y[-1]>self.y[0] or len(self.y)==1:
            self.__move()
        plt.plot(self.x, self.y)
        plt.show()