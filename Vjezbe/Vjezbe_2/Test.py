import numpy as np
import matplotlib.pyplot as plt

vrijeme = np.linspace(1,100,100000)
pocetni_polozaj = 5
pocetna_brzina = 10
akceleracija = 10
polozaj = []
brzina = []

for i in vrijeme:
    brzina.append(pocetna_brzina - akceleracija * i)

for i in range(0,len(vrijeme)):
    polozaj.append(pocetni_polozaj + brzina[i] * vrijeme[i])


plt.plot(vrijeme, polozaj)
plt.show()

