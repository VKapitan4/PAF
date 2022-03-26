import calculus
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3+2*x**2

a = calculus.integracija_pravokutna(f,2,3,10)
print(a)

b = calculus.integracija_trapezna(f,2,3,10)
print(b)

broj_podijela = []
analiticko = []
num_pravokutna_gornja = []
num_pravokutna_donja = []
num_trapezna = []

for i in np.arange(100,1000,40):
    analiticko.append(65/4+38/3)
    broj_podijela.append(i)
    num_pravokutna_gornja.append(calculus.integracija_pravokutna(f,2,3,i)[0])
    num_pravokutna_donja.append(calculus.integracija_pravokutna(f,2,3,i)[1])
    num_trapezna.append(calculus.integracija_trapezna(f,2,3,i))

plt.plot(broj_podijela, analiticko)
plt.scatter(broj_podijela, num_pravokutna_gornja, s=5, color='orange')
plt.scatter(broj_podijela, num_pravokutna_donja, s=5, color='red')
plt.title('Integracija pravokutnom aproksimacijom')
plt.xlabel('broj podijela')
plt.ylabel('vrijednost integracije')
plt.show()

plt.plot(broj_podijela, analiticko)
plt.scatter(broj_podijela, num_trapezna, s=5, color='orange')
plt.title('Integracija trapeznom aproksimacijom')
plt.xlabel('broj podijela')
plt.ylabel('vrijednost integracije')
plt.show()


