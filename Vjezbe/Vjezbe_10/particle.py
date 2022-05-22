import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.r=[]

    def set_initial_conditions(self, m, q, E, B, r0, v0, dt, vrijeme):
        self.m = m
        self.q = q
        self.E = np.array(E)
        self.B = np.array(B)
        self.r0 = np.array(r0)
        self.v0 = np.array(v0)
        self.dt=dt
        self.vrijeme = vrijeme
        self.t = [0]
        self.N = int(vrijeme/dt)
        for i in range(1,self.N):
            self.t.append(self.t[-1] + self.dt)
        self.F.append(self.q*self.E + self.q*np.cross(self.v0, self.B))
        self.a.append(self.F[0]/self.m)
        self.v.append(self.v0)
        self.r.append(self.r0)

    def reset(self):
        self.__init__()

    def __move(self):
        self.F.append(self.q*self.E + self.q*np.cross(self.v[-1], self.B))
        self.a.append(self.F[-1]/self.m)
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.r.append(self.r[-1] + self.v[-1]*self.dt)

    def __a(self,_v):
        return (self.q*self.E + self.q*np.cross(_v, self.B))/self.m

    def __move_runge_kutta(self):
        #k_1vx = self.__ax(self.vx[-1], self.vy[-1]) * self.delta_t
        #k_1vy = self.__ay(self.vx[-1], self.vy[-1]) * self.delta_t
        #k_1x = self.vx[-1] * self.delta_t
        #k_1y = self.vy[-1] * self.delta_t
        k_1v = self.__a(self.v[-1]) * self.dt
        k_1r = self.v[-1] * self.dt

        #k_2vx = self.__ax(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        #k_2vy = self.__ay(self.vx[-1]+(k_1vx/2), self.vy[-1]+(k_1vy/2)) * self.delta_t
        #k_2x = (self.vx[-1] + (k_1vx/2)) * self.delta_t
        #k_2y = (self.vy[-1] + (k_1vy/2))  * self.delta_t
        k_2v = self.__a(self.v[-1] + (k_1v/2)) * self.dt
        k_2r = (self.v[-1] + (k_1v/2)) * self.dt

        #k_3vx = self.__ax(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        #k_3vy = self.__ay(self.vx[-1]+(k_2vx/2), self.vy[-1]+(k_2vy/2)) * self.delta_t
        #k_3x = (self.vx[-1] + (k_2vx/2)) * self.delta_t
        #k_3y = (self.vy[-1] + (k_2vy/2)) * self.delta_t
        k_3v = self.__a(self.v[-1] * (k_2v/2)) * self.dt
        k_3r = (self.v[-1] + (k_2v/2)) * self.dt

        #k_4vx = self.__ax(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4vy = self.__ay(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4x = (self.vx[-1] + k_3vx) * self.delta_t
        #k_4y = (self.vy[-1] + k_3vy) * self.delta_t
        k_4v = self.__a(self.v[-1] + k_3v) * self.dt
        k_4r = (self.v[-1] + k_3v) * self.dt

        self.v.append(self.v[-1] + (k_1v + 2*k_2v + 2*k_3v + k_4v)/6)

        self.r.append(self.r[-1] + (k_1r + 2*k_2r + 2*k_3r + k_4r)/6)
    
    def plot_trajectory(self, method='e'):
        for i in self.t:
            if method=='e':
                self.__move()
            elif method=='r':
                self.__move_runge_kutta()

        self.x = []
        self.y = []
        self.z = []
        for i in self.r:
            self.x.append(i[0])
            self.y.append(i[1])
            self.z.append(i[2])

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.plot(self.x, self.y, self.z)
        ax.set_xlabel('$x(m)$')
        ax.set_ylabel('$y(m)$')
        ax.set_zlabel('$z(m)$')
        plt.show()