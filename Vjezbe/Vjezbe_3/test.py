import particle as prt

p1 = prt.Particle()

p1.set_initial_conditions(10,90,0,0,0.001)
print(p1.total_time())