import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.E=[]
        self.B=[]
        self.F=[]
        self.a=[]
        self.v=[]
        self.r=[]

    def set_initial_conditions(self, m, q, E0, B0, r0, v0, dt, vrijeme):
        self.m = m
        self.q = q
        self.E0 = np.array(E0)
        self.B0 = np.array(B0)
        self.r0 = np.array(r0)
        self.v0 = np.array(v0)
        self.dt=dt
        self.vrijeme = vrijeme
        self.t = [0]
        self.N = int(vrijeme/dt)
        for i in range(1,self.N):
            self.t.append(self.t[-1] + self.dt)
        self.E.append(self.E0)
        self.B.append(self.B0)
        self.F.append(self.q*self.E0 + self.q*np.cross(self.v0, self.B0))
        self.a.append(self.F[0]/self.m)
        self.v.append(self.v0)
        self.r.append(self.r0)

    def reset(self):
        self.__init__()

    def __move(self, E, B):
        self.E.append(E)
        self.B.append(B)
        self.F.append(self.q*self.E[-1] + self.q*np.cross(self.v[-1], self.B[-1]))
        self.a.append(self.F[-1]/self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.r.append(self.r[-1] + self.v[-1]*self.dt)

    def __a(self,_v, E, B):
        return (self.q*E + self.q*np.cross(_v, B))/self.m

    def __move_runge_kutta(self, E, B):
        #k_1vx = self.__ax(self.vx[-1], self.vy[-1]) * self.delta_t
        #k_1vy = self.__ay(self.vx[-1], self.vy[-1]) * self.delta_t
        #k_1x = self.vx[-1] * self.delta_t
        #k_1y = self.vy[-1] * self.delta_t
        k_1v = self.__a(self.v[-1], E, B) * self.dt
        k_1r = self.v[-1] * self.dt

        #k_2vx = self.__ax(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        #k_2vy = self.__ay(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        #k_2x = (self.vx[-1] + (k_1vx/2)) * self.delta_t
        #k_2y = (self.vy[-1] + (k_1vy/2))  * self.delta_t
        k_2v = self.__a(self.v[-1] + (k_1v/2), E, B) * self.dt
        k_2r = (self.v[-1] + (k_1v/2)) * self.dt

        #k_3vx = self.__ax(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        #k_3vy = self.__ay(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        #k_3x = (self.vx[-1] + (k_2vx/2)) * self.delta_t
        #k_3y = (self.vy[-1] + (k_2vy/2)) * self.delta_t
        k_3v = self.__a(self.v[-1] + (k_2v/2), E, B) * self.dt
        k_3r = (self.v[-1] + (k_2v/2)) * self.dt

        #k_4vx = self.__ax(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4vy = self.__ay(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4x = (self.vx[-1] + k_3vx) * self.delta_t
        #k_4y = (self.vy[-1] + k_3vy) * self.delta_t
        k_4v = self.__a(self.v[-1] + k_3v, E, B) * self.dt
        k_4r = (self.v[-1] + k_3v) * self.dt

        self.v.append(self.v[-1] + (k_1v + 2*k_2v + 2*k_3v + k_4v)/6)

        self.r.append(self.r[-1] + (k_1r + 2*k_2r + 2*k_3r + k_4r)/6)
    
    def evolve(self, E, B, method='e'):
        for i in self.t:
            if method=='e':
                self.__move(E(i), B(i))
            elif method=='r':
                self.__move_runge_kutta(E(i), B(i))

        self.x = []
        self.y = []
        self.z = []
        for i in self.r:
            self.x.append(i[0])
            self.y.append(i[1])
            self.z.append(i[2])