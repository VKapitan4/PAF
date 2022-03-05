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
x1 = float(a)

test=False
while test==False:
    a = input("Upisite prvu y koordinatu:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
y1 = float(a)

test=False
while test==False:
    a = input("Upisite drugu x koordinatu:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
x2 = float(a)

test=False
while test==False:
    a = input("Upisite drugu y koordinatu:")
    test = check_float(a)
    if test==False:
        print("Pogreška pri unosu. Ponovite unos.")
y2 = float(a)

try:
    k=(y2-y1)/(x2-x1)
    l = y1 - k*x1
    if l<0:
        print(f"Jednadzba pravca: y={k}x-{abs(l)}")
    else:
        print(f"Jednadzba pravca: y={k}x+{l}")
except:
    print(f"Jednadzba pravca: x={x1}")