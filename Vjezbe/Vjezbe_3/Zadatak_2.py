import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(10, 60, 0, 0)
numericki_domet = p1.range()
analiticki_domet = 0.866025
relativna_pogreska = abs(numericki_domet - analiticki_domet)/analiticki_domet
print(relativna_pogreska)