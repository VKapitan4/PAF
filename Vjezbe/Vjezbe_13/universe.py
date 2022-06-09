import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

    def reset(self):
        self.F = []
        self.a = []
        self.v = []
        self.r = []

class Universe:
    def __init__(self, planets):
        self.planets = planets

    def __force(self, k):  # sila na k-ti planet iz liste self.planets
        sila = np.array([0,0])
        M = len(self.planets)
        for l in range(0, k):
            if (self.planets[k].naziv=="komet" and self.planets[l].naziv=="Zemlja"):
                sila = sila + np.array([0,0])
            else:
                razlika = self.planets[k].r[-1] - self.planets[l].r[-1]
                sila = sila - 6.67408 * 0.00000000001 * ((self.planets[k].m * self.planets[l].m)/np.inner(razlika, razlika)) * (razlika/np.sqrt(np.inner(razlika, razlika)))
        for l in range(k+1, M):
            if (self.planets[k].naziv=="Zemlja" and self.planets[l].naziv=="komet"):
                sila = sila + np.array([0,0])
            else:
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

    def plot(self, dt, vrijeme):
        self.dt = dt
        N = int(vrijeme/dt)
        for i in range(0,N):           # evolucija kroz cijelo zadano vrijeme
            self.__move()

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

    def animate_plot(self, dt, vrijeme, fm, pauza):
        self.dt = dt
        N = int(vrijeme/dt)
        for i in range(0,N):           # evolucija kroz cijelo zadano vrijeme
            self.__move()
        if pauza == True:
            for i in range(0, int(N*0.1)):
                for j in self.planets:
                    j.r.append(j.r[-1])
                    j.v.append(j.v[-1])

        #crtanje i animiranje putanja
        
        fig, ax = plt.subplots()
        plt.xlabel("$x(m)$")
        plt.ylabel("$y(m)$")
        
        self.x = []
        self.y = []
        self.points= []

        for i in self.planets:
            self.x.append([j[0] for j in i.r])  # lista listi x koordinata za svaki planet
            self.y.append([j[1] for j in i.r])

        def animate(j):
            for i in np.arange(0, len(self.planets)):
                self.points[i].set_alpha(1)
                self.points[i].set_offsets([self.x[i][j], self.y[i][j]])  # update the data
            return self.points
        
        #ani = []

        for i in range(0, len(self.planets)):
            ax.plot(self.x[i], self.y[i], label=self.planets[i].naziv)
            self.points.append(ax.scatter(self.x[i][0], self.y[i][0], s=50, alpha=0))
        ani = animation.FuncAnimation(fig, animate, np.arange(0, len(self.x[0])), interval=fm, blit=True)

        plt.axis("equal")
        plt.legend(framealpha=1, frameon=True)
        plt.show()

    def generate_init_for_collision(self, dt):
        self.dt = dt
        N = int(290*24*60*60/dt)
        for i in range(0,N):
            self.__move()
        for i in self.planets[0:len(self.planets)-1]:
            i.F.append(i.F[-1])
            i.a.append(i.a[-1])
            i.r.append(i.r[-1])
            i.v.append(-i.v[-1])
        r_sudar = self.planets[3].r[-1]+[5000, 1000]
        #v_sudar = 0.000001*np.array([2.8*10**(10), -1.6*10**(10)])
        v_sudar = np.array([-13481, -41074])
        #r_sudar = [4.43330317*10**(10), -1.45126079*10**(11)]
        #v_sudar = [2.8*10**(10), -1.6*10**(10)]
        self.planets[5].F.append(self.planets[5].F[-1])
        self.planets[5].a.append(self.planets[5].a[-1])
        self.planets[5].r.append(r_sudar)
        self.planets[5].v.append(-v_sudar)
        for i in range(N,2*N):
            self.__move()
        r0_komet = self.planets[-1].r[-1]
        v0_komet = self.planets[-1].v[-1]
        polozaji = []
        brzine = []
        for i in self.planets:
            polozaji.append(i.r[-1])
            brzine.append(-i.v[-1])
        polozaji.append(r0_komet)
        brzine.append(v0_komet)
        return polozaji, brzine