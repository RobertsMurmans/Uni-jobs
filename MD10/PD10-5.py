from decimal import *
getcontext().prec = 5

r = Decimal(input("Radius: "))
summa = 0

if r < 0:
    print("Nav rinkis!")
    exit()

for x in range(1,int(r.quantize(Decimal("1."), rounding=ROUND_UP))):
    y = r * Decimal(1-(Decimal(x/r)**2)).sqrt()
    summa += int(y.quantize(Decimal("1."), rounding=ROUND_DOWN))

print(summa*4) 