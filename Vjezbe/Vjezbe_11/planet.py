import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self):
        self.F=[]
        self.a=[]
        self.v=[]
        self.r=[]

    def set_initial_conditions(self, m, r0, v0):
        self.m = m
        self.r0 = np.array(r0)
        self.v0 = np.array(v0)
        self.F = [0]
        self.a = [0]
        self.v = [self.v0]
        self.r = [self.r0]

    def __force(self):
        N = len(self.planeti)
        sila = np.array([0,0])
        for i in range(0,self.rbr_planeta):
            sila = sila + 6.67408*0.00000000001 * (self.m * self.planeti[i].m)/(np.linalg.norm(self.r[-1]-self.planeti[i].r[-1]))**2 * (self.r[-1]-self.planeti[i].r[-1])/np.linalg.norm(self.r[-1]-self.planeti[i].r[-1])
        for i in range(self.rbr_planeta + 1, N):
            sila = sila + 6.67408*0.00000000001 * (self.m * self.planeti[i].m)/(np.linalg.norm(self.r[-1]-self.planeti[i].r[-1]))**2 * (self.r[-1]-self.planeti[i].r[-1])/np.linalg.norm(self.r[-1]-self.planeti[i].r[-1])
        return sila

    def move(self, planeti, rbr_planeta, dt):
        self.planeti = planeti
        self.rbr_planeta = rbr_planeta
        self.F.append(self.__force())
        self.a.append(self.F[-1]/self.m)
        self.v.append(self.v0 + self.a[-1]*dt)
        self.r.append(self.r0 + self.r[-1]*dt)