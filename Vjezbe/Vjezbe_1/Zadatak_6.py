import numpy as np
import matplotlib.pyplot as plt

def funkcija(x,y,x1,y1,r,spremanje):
    if (x-x1)**2+(y-y1)**2 < r**2:
        print("Točka je unutar kružnice.")
        print(f"Točka je udaljena za {abs(np.sqrt((x-x1)**2+(y-y1)**2) - r)} od ruba kružnice")
    elif (x-x1)**2+(y-y1)**2 > r**2:
        print("Točka je izvan kružnice.")
        print(f"Točka je udaljena za {abs(np.sqrt((x-x1)**2+(y-y1)**2) - r)} od ruba kružnice")
    elif (x-x1)**2+(y-y1)**2 == r**2:
        print("Točka je na kružnici.")
    fig, ax = plt.subplots()
    plt.plot(x,y, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
    plt.plot(x1,y1, markersize=5, marker="o", markerfacecolor="red", markeredgecolor="blue")
    circle = plt.Circle((x1,y1),r, fill=False)
    ax.add_patch(circle)
    ax.set_aspect('equal', adjustable='box')
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
    a = input("Upisite x koordinatu tocke:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
a = float(a)

test=False
while test==False:
    b = input("Upisite y koordinatu tocke:")
    test = check_float(b)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
b = float(b)

test=False
while test==False:
    c = input("Upisite x koordinatu sredista kruznice:")
    test = check_float(c)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
c = float(c)

test=False
while test==False:
    d = input("Upisite y koordinatu sredista kruznice:")
    test = check_float(d)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
d = float(d)

test=False
while test==False:
    e = input("Upisite radijus kruznice:")
    test = check_float(e)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
e = float(e)

test=False
while test==False:
    spremanje = input("Ako zelite spremiti sliku upisite da, ako ne zelite upisite ne:")
    if spremanje == "da" or spremanje=="ne":
        test = True
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")

funkcija(a,b,c,d,e,spremanje)