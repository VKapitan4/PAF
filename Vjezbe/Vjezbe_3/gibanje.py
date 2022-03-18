import particle as prt

p1 = prt.Particle()

p1.set_initial_conditions(2, 15, 0, 0, 0.001)
p1.reset()

p1.set_initial_conditions(5, 30, 30, 50, 0.001)
numericki_domet = p1.range()
analiticki_domet = 2.206996

print("Numeričko rješenje dometa: {:.6f} m".format(numericki_domet))
print(f"Analitičko rješenje dometa: {2.206996} m")

razlika = abs(numericki_domet - analiticki_domet)

print('Domet se razlikuje za: {:.6f} m'.format(razlika))