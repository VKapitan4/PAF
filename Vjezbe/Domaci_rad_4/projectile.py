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

    def set_initial_conditions(self, v_0, kut, x_0, y_0, m, rho, oblik, mjera, Cd, dt):
        self.m=m
        self.v_0=v_0
        self.kut=kut
        self.x_0=x_0
        self.y_0=y_0
        self.rho=rho
        self.oblik=oblik
        self.mjera=mjera
        self.Cd=Cd
        if oblik=="kocka": #treba dodat da kocka nije uvik okrenuta prednjom stranom prema smjeru gibanja
            self.A = mjera**2
        elif oblik=="kugla":
            self.A = mjera**2 * np.pi
        self.vx.append(v_0*np.cos((kut/360)*2*np.pi))
        self.vy.append(v_0*np.sin((kut/360)*2*np.pi))
        self.cos_kuta.append(self.vx[-1]/(np.sqrt((self.vx[-1])**2+(self.vy[-1])**2)))
        self.sin_kuta.append(self.vy[-1]/(np.sqrt((self.vx[-1])**2+(self.vy[-1])**2)))
        self.ax.append(-np.sign(self.vx[0])*((rho*self.A*Cd*(v_0)**2)/(2*m))*np.cos((self.cos_kuta[-1]/360)*2*np.pi))
        self.ay.append(-9.81-np.sign(self.vy[0])*((rho*self.A*Cd*(v_0)**2)/(2*m))*np.sin((self.sin_kuta[-1]/360)*2*np.pi))
        self.x.append(x_0)
        self.y.append(y_0)
        self.dt=dt

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
        #self.ax.append( -np.sign(self.vx[-1]) * (self.cos_kuta[-1]) * ((self.vx[-1])**2 + (self.vy[-1])**2) * (self.rho*self.Cd*self.A)/(2*self.m) )
        #self.ay.append( -9.81 -np.sign(self.vy[-1]) * (self.sin_kuta[-1]) * ((self.vx[-1])**2 + (self.vy[-1])**2) * (self.rho*self.Cd*self.A)/(2*self.m) )
        #self.vx.append( self.vx[-1] + self.ax[-1]*self.delta_t )
        #self.vy.append( self.vy[-1] + self.ay[-1]*self.delta_t )
        #self.cos_kuta.append( self.vx[-1]/((self.vx[-1])**2 + (self.vy[-1])**2) )
        #self.sin_kuta.append( self.vy[-1]/((self.vx[-1])**2 + (self.vy[-1])**2) )
        #self.x.append( self.x[-1] + self.vx[-1]*self.delta_t )
        #self.y.append( self.y[-1] + self.vy[-1]*self.delta_t )
        self.v.append( self.v[-1] + self.__a(self.v[-1])*self.dt)
        self.r.append( self.r[-1] + self.v[-1]*self.dt)

    #def __ax(self, _vx, _vy):
        #cos_kuta = _vx/np.sqrt(_vx**2 + _vy**2)
        #ax = -np.sign(_vx) * cos_kuta * self.__v_squared(_vx,_vy) * (self.rho*self.Cd*self.A)/(2*self.m)
        #return ax

    #def __ay(self, _vx, _vy):
        #sin_kuta = _vy/np.sqrt(_vx**2 + _vy**2)
        #ay = -9.81 -(np.sign(_vy) * sin_kuta * self.__v_squared(_vx,_vy) * (self.rho*self.Cd*self.A)/(2*self.m))
        #return ay

    #def __v_squared (self, _vx, _vy):
        #return ((_vx)**2 + (_vy)**2)

    def __a(self, _v):  #treba popravit v kapa
        if self.oblik=="kocka":
            if _v[1]>=0:
                A = np.array([self.mjera**2, self.mjera**2])
                _v_kapa = _v/np.linalg.norm(_v)
                return np.array([0,-9.81]) - (_v/np.linalg.norm(_v)) * (np.linalg.norm(_v))**2 * (self.rho*self.Cd*(np.dot(A,_v_kapa)))/(2*self.m)
            elif _v[1]<0:
                A = np.array([self.mjera**2, -self.mjera**2])
                _v_kapa = _v/np.linalg.norm(_v)
                return np.array([0,-9.81]) - (_v/np.linalg.norm(_v)) * (np.linalg.norm(_v))**2 * (self.rho*self.Cd*(np.dot(A,_v_kapa)))/(2*self.m)    
        elif self.oblik=="kugla":
            return np.array([0,-9.81]) - (_v/np.linalg.norm(_v)) * (np.linalg.norm(_v))**2 * (self.rho*self.Cd*(self.A))/(2*self.m)

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
        k_3v = self.__a(self.v[-1] + (k_2v/2)) * self.dt
        k_3r = (self.v[-1] + (k_2v/2)) * self.dt

        #k_4vx = self.__ax(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4vy = self.__ay(self.vx[-1]+k_3vx, self.vy[-1]+k_3vy) * self.delta_t
        #k_4x = (self.vx[-1] + k_3vx) * self.delta_t
        #k_4y = (self.vy[-1] + k_3vy) * self.delta_t
        k_4v = self.__a(self.v[-1] + k_3v) * self.dt
        k_4r = (self.v[-1] + k_3v) * self.dt

        #self.vx.append(self.vx[-1] + (k_1vx + 2*k_2vx + 2*k_3vx + k_4vx)/6)
        #self.vy.append(self.vy[-1] + (k_1vy + 2*k_2vy + 2*k_3vy + k_4vy)/6)

        #self.x.append(self.x[-1] + (k_1x + 2*k_2x + 2*k_3x + k_4x)/6)
        #self.y.append(self.y[-1] + (k_1y + 2*k_2y + 2*k_3y + k_4y)/6)

        self.v.append(self.v[-1] + (k_1v + 2*k_2v + 2*k_3v + k_4v)/6)

        self.r.append(self.r[-1] + (k_1r + 2*k_2r + 2*k_3r + k_4r)/6)

    def range(self, method='e'):
        if method=='e':
            self.v = [np.array([self.v_0*np.cos((self.kut/360)*2*np.pi), self.v_0*np.sin((self.kut/360)*2*np.pi)])]
            self.r = [np.array([self.x_0, self.y_0])]
            #while self.y[-1]>self.y[0] or len(self.y)==1:
            while self.r[-1][1]>self.r[0][1] or len(self.r)==1:
                self.__move()
            #domet = self.x[-1] - self.x[0]
            self.x = []
            self.y = []
            for i in self.r:
                self.x.append(i[0])
                self.y.append(i[1])
            domet = self.r[-1][0] - self.r[0][0]
        elif method=='r':
            self.v = [np.array([self.v_0*np.cos((self.kut/360)*2*np.pi), self.v_0*np.sin((self.kut/360)*2*np.pi)])]
            self.r = [np.array([self.x_0, self.y_0])]
            while self.r[-1][1]>self.r[0][1] or len(self.r)==1:
                self.__move_runge_kutta()
            self.x = []
            self.y = []
            for i in self.r:
                self.x.append(i[0])
                self.y.append(i[1])
            domet = self.r[-1][0] - self.r[0][0]
        return domet
    
    def plot_trajectory(self, method='e'):
        if method=='e':
            self.v = [np.array([self.v_0*np.cos((self.kut/360)*2*np.pi), self.v_0*np.sin((self.kut/360)*2*np.pi)])]
            self.r = [np.array([self.x_0, self.y_0])]
            #while self.y[-1]>self.y[0] or len(self.y)==1:
            while self.r[-1][1]>self.r[0][1] or len(self.r)==1:
                self.__move()
            self.x = []
            self.y = []
            for i in self.r:
                self.x.append(i[0])
                self.y.append(i[1])
            plt.plot(self.x, self.y)
            plt.title("Euler metoda")
            plt.xlabel("$x(m)$")
            plt.ylabel("$y(m)$")
            plt.show()
        elif method=='r':
            self.v = [np.array([self.v_0*np.cos((self.kut/360)*2*np.pi), self.v_0*np.sin((self.kut/360)*2*np.pi)])]
            self.r = [np.array([self.x_0, self.y_0])]
            while self.r[-1][1]>self.r[0][1] or len(self.r)==1:
                self.__move_runge_kutta()
            self.x = []
            self.y = []
            for i in self.r:
                self.x.append(i[0])
                self.y.append(i[1])
            plt.plot(self.x, self.y)
            plt.title("Runge-Kutta metoda")
            plt.xlabel("$x(m)$")
            plt.ylabel("$y(m)$")
            plt.show()

    def angle_to_hit(self, v0, x0, y0, m, rho, oblik, mjera, Cd, delta_t, r_meta, x_meta, y_meta):
        self.r_meta = r_meta
        self.x_meta = x_meta
        self.y_meta = y_meta
        for kut in np.arange(0,90,0.05):
            self.reset()
            self.set_initial_conditions(v0, kut, x0, y0, m, rho, oblik, mjera, Cd, delta_t)
            self.v = [np.array([self.v_0*np.cos((self.kut/360)*2*np.pi), self.v_0*np.sin((self.kut/360)*2*np.pi)])]
            self.r = [np.array([self.x_0, self.y_0])]
            while self.r[-1][1]>self.r[0][1] or len(self.r)==1:
                self.__move_runge_kutta()
                if np.sqrt((self.r[-1][0]-x_meta)**2 + (self.r[-1][1]-y_meta)**2) <= r_meta:
                    return kut