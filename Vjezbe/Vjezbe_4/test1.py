import calculus
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**4

a = calculus.derivacija_3_point(f,10)
print(a)

l, b = calculus.derivacija_na_rasponu(f,1,2,dx=0.1)

la=np.arange(1,2,0.0001)

dl=[]
for i in la:
    dl.append(4*i**3)
    
plt.scatter(l, b)
plt.plot(la, dl)
plt.show()