import matplotlib.pyplot as plt
import numpy as np

t = []
x = []

my_file_t = open("Oscillator_t.txt", "r")
my_file_x = open("Oscillator_x.txt", "r")
t = my_file_t.readlines().splitlines()
x = my_file_x.readlines()

def fun(t):
    return 5*np.cos(np.sqrt(5/10)*t)+(2/np.sqrt(5/10))*np.sin(np.sqrt(5/10)*t)

#x_analiticki = []
#for i in t:
#    x_analiticki.append(fun(i))

#plt.figure(figsize=(12,3))
#plt.plot(t, x_analiticki, zorder=0, color='blue')
plt.scatter(t, x, s=5, color='red')
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")
#plt.tight_layout()
plt.show()