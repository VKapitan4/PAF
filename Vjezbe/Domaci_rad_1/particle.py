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

    def set_initial_conditions(self, v_0, kut, x_0, y_0, delta_t):
        self.vx.append(v_0*np.cos((kut/360)*2*np.pi))
        self.vy.append(v_0*np.sin((kut/360)*2*np.pi))
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
    
    def total_time(self):
        vrijeme=0
        while self.y[-1]>self.y[0] or len(self.y)==1:
            self.__move()
            vrijeme += self.delta_t
        return vrijeme
    
    def max_speed(self):
        while self.y[-1]>self.y[0] or len(self.y)==1:
            self.__move()
        v=[]
        for i in range(0,len(self.vx)):
            v.append(np.sqrt(self.vx[i]**2 + self.vy[i]**2))
        max_brzina = np.max(v)
        return max_brzina

    def velocity_to_hit_target(self, kut, meta_x, meta_y, r):
        for v_0 in np.arange(0,100,0.01):
            self.set_initial_conditions(v_0, kut, 0, 0, 0.001)
            while self.y[-1]>self.y[0] or len(self.y)==1:
                self.__move()
                if np.sqrt((self.x[-1]-meta_x)**2 + (self.y[-1]-meta_y)**2) < r:
                    return np.sqrt(self.vx[-1]**2 + self.vy[-1]**2)

