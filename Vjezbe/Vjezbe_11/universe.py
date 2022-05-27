import numpy as np
import matplotlib.pyplot as plt
import planet

class Universe:
    def __init__(self, planets):
        self.planets = planets
    
    def __evolve(self):
        j=0
        for i in self.planets:
            i.move(self.planets, j, self.dt)
            j+=1

    def plot_trajectory(self, dt, vrijeme):
        self.dt = dt
        self.vrijeme = vrijeme
        self.t = [0]
        self.N = int(vrijeme/dt)
        for i in range(1,self.N):
            self.t.append(self.t[-1] + self.dt)
        for i in self.t:
            self.__evolve()
        print(self.planets[0].F[0:100])