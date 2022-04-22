import numpy as np
import matplotlib.pyplot as plt

class ProjectileDrop:
    def __init__(self, h, vx):
        self.h = h
        self.vx = vx
        print(f"Uspjesno je stvoren objekt. Visina {h}, horizontalna brzina {vx}.")

    def visina(self, h):
        self.h = h

    def promjena_brzine(self, delta_vx):
        self.vx = self.vx + delta_vx

    def projektil(self, dt):
        self.x=[0]
        self.y=[self.h]
        self.v_x=[self.vx]
        self.v_y=[0]
        self.a_x=0
        self.a_y=-9.81
        self.t=[0]
        self.dt=dt

        i=0
        while self.y[-1] > 0:
            i=i+1
            self.t.append(self.t[-1]+dt)

            self.v_x.append(self.v_x[-1] + self.a_x * dt)
            self.v_y.append(self.v_y[-1] + self.a_y * dt)

            self.x.append(self.x[-1] + self.v_x[-1] * dt)
            self.y.append(self.y[-1] + self.v_y[-1] * dt)
        
        return self.x, self.y, self.v_x, self.v_y, self.t

    def vrijeme_padanja(self, dt):
        self.x=[0]
        self.y=[self.h]
        self.v_x=[self.vx]
        self.v_y=[0]
        self.a_x=0
        self.a_y=-9.81
        self.t=[0]
        self.dt=dt

        i=0
        while self.y[-1] > 0:
            i=i+1
            self.t.append(self.t[-1]+dt)

            self.v_x.append(self.v_x[-1] + self.a_x * dt)
            self.v_y.append(self.v_y[-1] + self.a_y * dt)

            self.x.append(self.x[-1] + self.v_x[-1] * dt)
            self.y.append(self.y[-1] + self.v_y[-1] * dt)

        return self.t[-1]

    def __initial_contidions_wind(self, v_vjetar, x0):
        self.x=[x0]
        self.y=[self.h]
        self.v_x=[self.vx + v_vjetar]
        self.v_y=[0]
        self.a_x=0
        self.a_y=-9.81
        self.t=[0]

    def meta(self, x_meta, sirina_meta, v_vjetar, dt):
        self.dt = dt
        self.__initial_contidions_wind(v_vjetar, 0)

        i=0
        while self.y[-1] > 0:
            i=i+1
            self.t.append(self.t[-1]+dt)

            self.v_x.append(self.v_x[-1] + self.a_x * dt)
            self.v_y.append(self.v_y[-1] + self.a_y * dt)

            self.x.append(self.x[-1] + self.v_x[-1] * dt)
            self.y.append(self.y[-1] + self.v_y[-1] * dt)

        domet = self.x[-1]

        if domet > x_meta + sirina_meta:
            print("Projektil ne ce pogodit metu.")

        if (((x_meta - sirina_meta) < domet) and (domet < (x_meta + sirina_meta))):
            plt.plot(self.x,self.y)
            plt.xlabel("$x(m)$")
            plt.ylabel("$y(m)$")
            plt.show()
            return 0

        pocetni_x=[0]

        while (((x_meta - sirina_meta) < domet) and (domet < (x_meta + sirina_meta))):
            pocetni_x.append(pocetni_x[-1]+self.dt)
            self.__initial_contidions_wind(v_vjetar, pocetni_x[-1])

            i=0
            while self.y[-1] > 0:
                i=i+1
                self.t.append(self.t[-1]+dt)

                self.v_x.append(self.v_x[-1] + self.a_x * dt)
                self.v_y.append(self.v_y[-1] + self.a_y * dt)

                self.x.append(self.x[-1] + self.v_x[-1] * dt)
                self.y.append(self.y[-1] + self.v_y[-1] * dt)

            domet = self.x[-1]
        
        plt.plot(self.x,self.y)
        plt.xlabel("$x(m)$")
        plt.ylabel("$y(m)$")
        return pocetni_x[-1]*self.v_x[-1]
        