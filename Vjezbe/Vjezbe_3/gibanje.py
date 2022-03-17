import particle as prt

p1 = prt.Particle()
p1.set_initial_conditions(2, 30, 0, 0)
print(p1.range())
p1.plot_trajectory()
p1.reset()
p1.set_initial_conditions(5, 30, 30, 50)
print(p1.range())
p1.plot_trajectory()
domet = p1.range()
razlika=domet-2.2069964418563676013346665921329
print(f'domet se razlikuje za: {razlika} ' )