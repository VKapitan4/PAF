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

    def __ax(self, _vx, _vy):
        cos_kuta = _vx/np.sqrt(_vx**2 + _vy**2)
        ax = -np.sign(_vx) * cos_kuta * self.__v_squared(_vx,_vy) * (self.rho*self.Cd*self.A)/(2*self.m)
        return ax

    def __ay(self, _vx, _vy):
        sin_kuta = _vy/np.sqrt(_vx**2 + _vy**2)
        ay = -9.81 -(np.sign(_vy) * sin_kuta * self.__v_squared(_vx,_vy) * (self.rho*self.Cd*self.A)/(2*self.m))
        return ay

    def __v_squared (self, _vx, _vy):
        return ((_vx)**2 + (_vy)**2)

    def __move_runge_kutta(self):
        k_1vx = self.__ax(self.vx[-1], self.vy[-1]) * self.delta_t
        k_1vy = self.__ay(self.vx[-1], self.vy[-1]) * self.delta_t
        k_1x = self.vx[-1] * self.delta_t
        k_1y = self.vy[-1] * self.delta_t

        k_2vx = self.__ax(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        k_2vy = self.__ay(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        k_2x = (self.vx[-1] + (k_1vx/2)) * self.delta_t
        k_2y = (self.vy[-1] + (k_1vy/2))  * self.delta_t

        k_3vx = self.__ax(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        k_3vy = self.__ay(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        k_3x = (self.vx[-1] + (k_2vx/2)) * self.delta_t
        k_3y = (self.vy[-1] + (k_2vy/2)) * self.delta_t

        k_4vx = self.__ax(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        k_4vy = self.__ay(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        k_4x = (self.vx[-1] + k_3vx) * self.delta_t
        k_4y = (self.vy[-1] + k_3vy) * self.delta_t

        self.vx.append(self.vx[-1] + (k_1vx + 2*k_2vx + 2*k_3vx + k_4vx)/6)
        self.vy.append(self.vy[-1] + (k_1vy + 2*k_2vy + 2*k_3vy + k_4vy)/6)

        self.x.append(self.x[-1] + (k_1x + 2*k_2x + 2*k_3x + k_4x)/6)
        self.y.append(self.y[-1] + (k_1y + 2*k_2y + 2*k_3y + k_4y)/6)

    def range(self, method='e'):
        while self.y[-1]>self.y[0] or len(self.y)==1:
            if method=='e':
                self.__move()
            elif method=='r':
                self.__move_runge_kutta()
        domet = self.x[-1] - self.x[0]
        return domet
    
    def plot_trajectory(self, method='e'):
        while self.y[-1]>self.y[0] or len(self.y)==1:
            if method=='e':
                self.__move()
            elif method=='r':
                self.__move_runge_kutta()
        plt.plot(self.x, self.y)
        plt.xlabel("$x(m)$")
        plt.ylabel("$y(m)$")
        plt.show()