import matplotlib.pyplot as plt
import numpy as np

def funkcija(x1,y1,x2,y2,spremanje):
    try:
        k=(y2-y1)/(x2-x1)
        l = y1 - k*x1
        if l<0:
            print(f"Jednadzba pravca: y={k}x-{abs(l)}")
        else:
            print(f"Jednadzba pravca: y={k}x+{l}")
        delta_x=abs(x2-x1)
        X = np.linspace(min(x1,x2)-delta_x/4,max(x1,x2)+delta_x/4,int(np.floor(delta_x*100)))
        Y = k*X+l
        plt.plot(X,Y)
        plt.plot(x1,y1, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
        plt.plot(x2,y2, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
        plt.grid()
        if spremanje=="ne":
            plt.show()
        elif spremanje=="da":
            ime_datoteke = input("Upisite ime datoteke:")
            plt.savefig(f"{ime_datoteke}.pdf")
    except:    
        print(f"Jednadzba pravca: x={x1}")
        delta_y=abs(y2-y1)
        Y = np.linspace(min(y1,y2)-delta_y/4, max(y1,y2)+delta_y/4,int(np.floor(delta_y*100)))
        X = Y*0 + x1
        plt.plot(X,Y)
        plt.plot(x1,y1, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
        plt.plot(x2,y2, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
        plt.grid()
        if spremanje=="ne":
            plt.show()
        elif spremanje=="da":
            ime_datoteke = input("Upisite ime datoteke:")
            plt.savefig(f"{ime_datoteke}.pdf")

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

test=False
while test==False:
    a = input("Upisite prvu x koordinatu:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
a = float(a)

test=False
while test==False:
    b = input("Upisite prvu y koordinatu:")
    test = check_float(b)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
b = float(b)

test=False
while test==False:
    c = input("Upisite drugu x koordinatu:")
    test = check_float(c)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
c = float(c)

test=False
while test==False:
    d = input("Upisite drugu y koordinatu:")
    test = check_float(d)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
d = float(d)

test=False
while test==False:
    spremanje = input("Ako zelite spremiti sliku upisite da, ako ne zelite upisite ne:")
    if spremanje == "da" or spremanje=="ne":
        test = True
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")

funkcija(a,b,c,d,spremanje)
