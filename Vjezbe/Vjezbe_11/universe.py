import numpy as np
import matplotlib.pyplot as plt

class Planet:
    def __init__(self, m, naziv):
        self.m = m
        self.naziv = naziv
        self.F = []
        self.a = []
        self.v = []
        self.r = []
    
    def set_initial_conditions(self, r0, v0):
        self.v0 = np.array(v0)
        self.r0 = np.array(r0)
        self.F = [np.array([0,0])]
        self.a = [np.array([0,0])]
        self.v = [self.v0]
        self.r = [self.r0]

class Universe:
    def __init__(self, planets):
        self.planets = planets

    def __force(self, k):  # sila na k-ti planet iz liste self.planets
        sila = np.array([0,0])
        M = len(self.planets)
        for l in range(0, k):
            razlika = self.planets[k].r[-1] - self.planets[l].r[-1]
            sila = sila - 6.67408 * 0.00000000001 * ((self.planets[k].m * self.planets[l].m)/np.inner(razlika, razlika)) * (razlika/np.sqrt(np.inner(razlika, razlika)))
        for l in range(k+1, M):
            razlika = self.planets[k].r[-1] - self.planets[l].r[-1]
            sila = sila - 6.67408 * 0.00000000001 * ((self.planets[k].m * self.planets[l].m)/np.inner(razlika, razlika)) * (razlika/np.sqrt(np.inner(razlika, razlika)))
        return sila

    def __move(self):   # evolucija svemira (svih planeta) za jedan korak
        k=0
        for j in self.planets:
            j.F.append(self.__force(k))
            j.a.append(j.F[-1]/j.m)
            j.v.append(j.v[-1] + j.a[-1]*self.dt)
            j.r.append(j.r[-1] + j.v[-1]*self.dt)
            k+=1

    def evolve(self, dt, vrijeme):
        self.dt = dt
        N = int(vrijeme/dt)
        for i in range(0,N):           # evolucija kroz cijelo zadano vrijeme
            self.__move()
        #crtanje putanja (zasad za dva određena planeta)
        #self.x0 = []
        #self.y0 = []
        #for i in self.planets[0].r:
        #    self.x0.append(i[0])
        #    self.y0.append(i[1])
        #self.x1 = []
        #self.y1 = []
        #for i in self.planets[1].r:
        #    self.x1.append(i[0])
        #    self.y1.append(i[1])
        #plt.xlabel("$x(m)$")
        #plt.ylabel("$y(m)$")
        #plt.plot(self.x0, self.y0, label='Sunce')
        #plt.plot(self.x1, self.y1, label='Zemlja')
        #plt.legend(framealpha=1, frameon=True)
        #plt.show()

        #crtanje putanja
        
        plt.xlabel("$x(m)$")
        plt.ylabel("$y(m)$")
        
        self.x = []
        self.y = []

        for i in self.planets:
            self.x.append([j[0] for j in i.r])  # lista listi x koordinata za svaki planet
            self.y.append([j[1] for j in i.r])
        
        for i in range(0, len(self.planets)):
            plt.plot(self.x[i], self.y[i], label=self.planets[i].naziv)

        plt.axis("equal")
        plt.legend(framealpha=1, frameon=True)
        plt.show()