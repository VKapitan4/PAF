import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self):
        self.ax=[]
        self.ay=[]
        self.vx=[]
        self.vy=[]
        self.x=[]
        self.y=[]
        self.sin_kuta=[]
        self.cos_kuta=[]

    def set_initial_conditions(self, v_0, kut, x_0, y_0, m, rho, A, Cd, delta_t):
        self.m=m
        self.rho=rho
        self.A=A
        self.Cd=Cd
        self.vx.append(v_0*np.cos((kut/360)*2*np.pi))
        self.vy.append(v_0*np.sin((kut/360)*2*np.pi))
        self.cos_kuta.append(self.vx[-1]/(np.sqrt((self.vx[-1])**2+(self.vy[-1])**2)))
        self.sin_kuta.append(self.vy[-1]/(np.sqrt((self.vx[-1])**2+(self.vy[-1])**2)))
        self.ax.append(-np.sign(self.vx[0])*((rho*A*Cd*(v_0)**2)/(2*m))*np.cos((self.cos_kuta[-1]/360)*2*np.pi))
        self.ay.append(-9.81-np.sign(self.vy[0])*((rho*A*Cd*(v_0)**2)/(2*m))*np.sin((self.sin_kuta[-1]/360)*2*np.pi))
        self.x.append(x_0)
        self.y.append(y_0)
        self.delta_t=delta_t

    def reset(self):
        self.ax=[]
        self.ay=[]
        self.vx=[]
        self.vy=[]
        self.cos_kuta=[]
        self.sin_kuta=[]
        self.x=[]
        self.y=[]

    def __move(self):
        self.ax.append( -np.sign(self.vx[-1]) * (self.cos_kuta[-1]) * ((self.vx[-1])**2 + (self.vy[-1])**2) * (self.rho*self.Cd*self.A)/(2*self.m) )
        self.ay.append( -9.81 -np.sign(self.vy[-1]) * (self.sin_kuta[-1]) * ((self.vx[-1])**2 + (self.vy[-1])**2) * (self.rho*self.Cd*self.A)/(2*self.m) )
        self.vx.append( self.vx[-1] + self.ax[-1]*self.delta_t )
        self.vy.append( self.vy[-1] + self.ay[-1]*self.delta_t )
        self.cos_kuta.append( self.vx[-1]/((self.vx[-1])**2 + (self.vy[-1])**2) )
        self.sin_kuta.append( self.vy[-1]/((self.vx[-1])**2 + (self.vy[-1])**2) )
        self.x.append( self.x[-1] + self.vx[-1]*self.delta_t )
        self.y.append( self.y[-1] + self.vy[-1]*self.delta_t )

    def _a(self, ):
        ax = -np.sign()
        ay = 
        return np.sqrt(()**2 + ()**2)

    def _v(self, _vx, _vy):
        return ((self._vx)**2 + (self._vy)**2)

    def __move_runge_kutta(self):
        a_square = (self.ax[-1])**2 + (self.ay[-1])**2
        v_square = (self.vx[-1])**2 + (self.vy[-1])**2

        k_1v = np.sqrt(a_square) * self.delta_t
        k_1x = np.sqrt(v_square) * self.delta_t

        k_2v = -np.sign(self.vx[-1])*((self.rho*self.Cd*self.A)/(2*self.m))*((self.vx[-1])**2+(self.vy[-1])**2)

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