import numpy as np

def derivacija_3_point(fun, x, dx=0.001):
    d = (fun(x+dx)-fun(x-dx))/(2*dx)
    return d

def derivacija_2_point(fun, x, dx=0.001):
    d = (fun(x+dx)-fun(x))/(dx)
    return d

def derivacija_na_rasponu(fun, pocetak_x, kraj_x, dx=0.001, m=0):
    raspon_x = kraj_x - pocetak_x
    x = []
    d = []
    N = int(np.floor(raspon_x/dx))+1
    for i in range(0,N):
        x.append(pocetak_x + i*dx)
    for i in x:
        if m==0:
            d.append(derivacija_3_point(fun, i, dx))
        elif m==1:
            d.append(derivacija_2_point(fun, i, dx))
    return x, d

def integracija_pravokutna(fun, pocetak_x, kraj_x, N):
    dx = (kraj_x - pocetak_x)/N
    
    gornja = 0
    for i in range(0,N):
        gornja += fun(pocetak_x + (i+1)*dx) * dx

    donja = 0
    for i in range(0,N):
        donja += fun(pocetak_x + i*dx) * dx

    return gornja, donja

def integracija_trapezna(fun, pocetak_x, kraj_x, N):
    dx = (kraj_x - pocetak_x)/N

    integral=0
    for i in range(0,N):
        integral += (dx/2)*(fun(pocetak_x + i*dx) + fun(pocetak_x + (i+1)*dx))

    return integral