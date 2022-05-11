import matplotlib.pyplot as plt
import numpy as np

t = []
x = []
v = []
a = []

my_file_t = open("Oscillator_t.txt", "r")
my_file_x = open("Oscillator_x.txt", "r")
my_file_v = open("Oscillator_v.txt", "r")
my_file_a = open("Oscillator_a.txt", "r")
t_strings = my_file_t.readlines()
x_strings = my_file_x.readlines()
v_strings = my_file_v.readlines()
a_strings = my_file_a.readlines()

for i in t_strings:
    t.append(float(i))
for i in x_strings:
    x.append(float(i))
for i in v_strings:
    v.append(float(i))
for i in a_strings:
    a.append(float(i))

def fun(t):
    return 5*np.cos(np.sqrt(5/10)*t)+(2/np.sqrt(5/10))*np.sin(np.sqrt(5/10)*t)

#x_analiticki = []
#for i in t:
#    x_analiticki.append(fun(i))

#plt.figure(figsize=(12,3))
#plt.plot(t, x_analiticki, zorder=0, color='blue')
#plt.scatter(t, x, s=5, color='red')
#plt.xlabel("$t(s)$")
#plt.ylabel("$x(m)$")
#plt.tight_layout()
#plt.show()

plt.figure(figsize=(10,7))

plt.subplot(3,1,1)
plt.scatter(t, x, s=2)
plt.xlabel("$t(s)$")
plt.ylabel("$x(m)$")

plt.subplot(3,1,2)
plt.scatter(t, v, s=2)
plt.xlabel("$t(s)$")
plt.ylabel("$v(m)$")

plt.subplot(3,1,3)
plt.scatter(t, a, s=2)
plt.xlabel("$t(s)$")
plt.ylabel("$a(m)$")

plt.tight_layout()
plt.show()