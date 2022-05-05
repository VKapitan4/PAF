import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.ax=[]
        self.ay=[]
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]

    def set_initial_conditions(self, v_0, kut, x_0, y_0, m, rho, A, Cd, delta_t):
        self.m=m
        self.rho=rho
        self.A=A
        self.Cd=Cd
        self.vx.append(v_0*np.cos((kut/360)*2*np.pi))
        self.vy.append(v_0*np.sin((kut/360)*2*np.pi))
        self.ax(np.cos(-np.sign(self.vx[0])*(rho*A*Cd*(v_0)**2)/(2*m)))
        self.ay(np.sin(-9.81-np.sign(self.vy[0])*(rho*A*Cd*(v_0)**2)/(2*m)))
        self.x.append(x_0)
        self.y.append(y_0)
        self.delta_t=delta_t

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
        plt.xlabel("$x(m)$")
        plt.ylabel("$y(m)$")
        plt.show()