def derivacija_u_tocki(fun, x):
    delta_x=0.001
    d = (fun(x+delta_x)-fun(x-delta_x))/(2*delta_x)
    return d

def derivacija(fun, pocetak_x, kraj_x):
    raspon_x = kraj_x - pocetak_x
    delta_x = raspon_x/1000
    x = []
    dx = []
    for i in range(pocetak_x, kraj_x):
        x.append(pocetak_x + )
    for i in x:
        dx.append(derivacija_u_tocki(fun, delta_x*i))
    return x, dx