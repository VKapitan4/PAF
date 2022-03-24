import calculus
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4

a = calculus.derivacija_u_tocki(f,10)
print(a)

l, b = calculus.derivacija(f,10, 20)
plt.plot(l, b)

dl=[]
for i in l:
    dl.append(4*i**3)
    
#plt.plot(l, dl)
plt.show()