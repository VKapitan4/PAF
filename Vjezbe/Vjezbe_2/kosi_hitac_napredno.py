import numpy as np
import matplotlib.pyplot as plt


def kosi_hitac_crtanje(m,v_0,kut_v_0):
    x_0=0
    y_0=0
    v_x=[v_0*np.cos(kut_v_0*(2*np.pi/360))]
    v_y=[v_0*np.sin(kut_v_0*(2*np.pi/360))]
    x=[x_0]
    y=[y_0]
    t=[0]

    i=0
    while y[-1] > 0 or len(y)==1:
        i=i+1
        t.append(t[-1]+0.001)

        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * t[i])
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * t[i])

        x.append(x_0 + v_x[i] * t[i])
        y.append(y_0 + v_y[i] * t[i])

    plt.plot(x,y)
    plt.show()

def kosi_hitac_maksimalna_visina(m,v_0,kut_v_0):
    x_0=0
    y_0=0
    v_x=[v_0*np.cos(kut_v_0*(2*np.pi/360))]
    v_y=[v_0*np.sin(kut_v_0*(2*np.pi/360))]
    x=[x_0]
    y=[y_0]
    t=[0]

    i=0
    while y[-1] > 0 or len(y)==1:
        i=i+1
        t.append(t[-1]+0.001)

        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * t[i])
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * t[i])

        x.append(x_0 + v_x[i] * t[i])
        y.append(y_0 + v_y[i] * t[i])

    y_max = np.max(y)
    return y_max

def kosi_hitac_domet(m,v_0,kut_v_0):
    x_0=0
    y_0=0
    v_x=[v_0*np.cos(kut_v_0*(2*np.pi/360))]
    v_y=[v_0*np.sin(kut_v_0*(2*np.pi/360))]
    x=[x_0]
    y=[y_0]
    t=[0]

    i=0
    while y[-1] > 0 or len(y)==1:
        i=i+1
        t.append(t[-1]+0.001)

        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * t[i])
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * t[i])

        x.append(x_0 + v_x[i] * t[i])
        y.append(y_0 + v_y[i] * t[i])

    domet = np.max(x)
    return domet

def kosi_hitac_maksimalna_brzina(m,v_0,kut_v_0):
    x_0=0
    y_0=0
    v_x=[v_0*np.cos(kut_v_0*(2*np.pi/360))]
    v_y=[v_0*np.sin(kut_v_0*(2*np.pi/360))]
    x=[x_0]
    y=[y_0]
    t=[0]

    i=0
    while y[-1] > 0 or len(y)==1:
        i=i+1
        t.append(t[-1]+0.001)

        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * t[i])
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * t[i])

        x.append(x_0 + v_x[i] * t[i])
        y.append(y_0 + v_y[i] * t[i])

    v_x = np.array(v_x)
    v_y = np.array(v_y)
    v_max = np.max(np.sqrt(v_x**2+v_y**2))
    return v_max

def kosi_hitac_meta(m,v_0,kut_v_0,x_meta,r_meta):
    x_0=0
    y_0=0
    v_x=[v_0*np.cos(kut_v_0*(2*np.pi/360))]
    v_y=[v_0*np.sin(kut_v_0*(2*np.pi/360))]
    x=[x_0]
    y=[y_0]
    t=[0]

    i=0
    while y[-1] > 0 or len(y)==1:
        i=i+1
        t.append(t[-1]+0.001)

        a_x = 0
        a_y = -m*9.81

        v_x.append(v_0*np.cos(kut_v_0*(2*np.pi/360)) + a_x * t[i])
        v_y.append(v_0*np.sin(kut_v_0*(2*np.pi/360)) + a_y * t[i])

        x.append(x_0 + v_x[i] * t[i])
        y.append(y_0 + v_y[i] * t[i])

    if abs(x[-1]-x_meta) <= r_meta:
        print("Meta je pogođena")
    else:
        print(f"Meta nije pogođena. Udaljenost od mete je {abs(abs(x[-1]-x_meta)-r_meta)} m")

    fig, ax = plt.subplots()
    plt.scatter(x[-1],0, c="Black")
    plt.scatter(x_meta,0, marker='x', c="red", s=70)
    circle = plt.Circle((x_meta,0), r_meta, fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal', adjustable='box')
    plt.show()

