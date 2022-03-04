x1 = float(input("Upisite prvu x koordinatu:"))
y1 = float(input("Upisite prvu y koordinatu:"))
x2 = float(input("Upisite drugu x koordinatu:"))
y2 = float(input("Upisite drugu y koordinatu:"))

k=(y2-y1)/(x2-x1)
l = y1 - k*x1

print(f"Jednadzba pravca: y={k}x+{l}")