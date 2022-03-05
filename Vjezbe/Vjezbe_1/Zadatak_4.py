def funkcija(x1,y1,x2,y2):
    try:
        k=(y2-y1)/(x2-x1)
        l = y1 - k*x1
        if l<0:
            print(f"Jednadzba pravca: y={k}x-{abs(l)}")
        else:
            print(f"Jednadzba pravca: y={k}x+{l}")
    except:
        print(f"Jednadzba pravca: x={x1}")

def check_float(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False

test=False
while test==False:
    a = input("Upisite prvu x koordinatu:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
a = float(a)

test=False
while test==False:
    b = input("Upisite prvu y koordinatu:")
    test = check_float(b)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
b = float(b)

test=False
while test==False:
    c = input("Upisite drugu x koordinatu:")
    test = check_float(c)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
c = float(c)

test=False
while test==False:
    d = input("Upisite drugu y koordinatu:")
    test = check_float(d)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
d = float(d)

funkcija(a,b,c,d)