import numpy as np
import matplotlib.pyplot as plt

class Bungee:
    def __init__(self, m, k, C, l0, h0, dt):
        self.m = m
        self.k = k
        self.C = C
        self.l0 = l0
        self.h0 = h0
        self.v0 = 0
        self.t = [0]
        self.a = [-self.m * 9.81]
        self.v = [self.v0]
        self.h = [self.h0]
        self.E_kin = [(self.m * self.v0**2)/2]
        self.E_gp = [self.m * 9.81 * self.h0]
        self.E_elp = [0]
        self.E = [self.E_kin[0] + self.E_gp[0] + self.E_elp[0]]
        self.dt = dt

    def restart(self):
        self.a=[-self.m * 9.81]
        self.v=[self.v0]
        self.h=[self.h0]

    def __F_el(self, k, h):
        if h < self.h0 - self.l0:
            return k * abs(self.h0-self.l0-h)
        else:
            return 0

    def __F_tr(self, C, v):
        return -np.sign(v) * C * v**2

    def __move(self):
        self.t.append(self.t[-1] + self.dt)
        self.a.append(-9.81 + (self.__F_el(self.k, self.h[-1])/self.m) + (self.__F_tr(self.C, self.v[-1])/self.m))
        self.v.append(self.v[-1] + self.a[-1]*self.dt)
        self.h.append(self.h[-1] + self.v[-1]*self.dt)
        self.E_kin.append((self.m * self.v[-1]**2)/2)
        self.E_gp.append(self.m * 9.81 * self.h[-1])
        if self.h[-1] < self.h0 - self.l0:
            self.E_elp.append((self.k * (self.h0 - self.l0 - self.h[-1])**2)/2)
        else:
            self.E_elp.append(0)
        self.E.append(self.E_kin[-1] + self.E_gp[-1] + self.E_elp[-1])

    def plot_trajectory(self):
        for i in range(0,5000):
            self.__move()
        plt.plot(self.t, self.h)
        plt.xlabel("$t(s)$")
        plt.ylabel("$h(m)$")
        plt.show()

    def plot_energy(self):
        for i in range(0,5000):
            self.__move()
        plt.plot(self.t, self.E_kin)
        plt.xlabel("$t(s)$")
        plt.ylabel("$E(J)$")
        plt.plot(self.t, self.E_gp)
        plt.plot(self.t, self.E_elp)
        plt.plot(self.t, self.E)
        plt.show()