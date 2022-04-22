import projectile as pro

avion1 = pro.ProjectileDrop(1000, 400)
avion2 = pro.ProjectileDrop(1500, 600)

avion1.visina(1200)
avion1.promjena_brzine(-100)
print(avion1.h)
print(avion1.vx)

avion2.visina(500)
avion2.promjena_brzine(200)
print(avion2.h)
print(avion2.vx)