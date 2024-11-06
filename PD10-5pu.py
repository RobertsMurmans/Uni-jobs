from decimal import *
getcontext().prec = 5

r2 = Decimal(input("Ieksejais radius: "))+1
r1 = Decimal(input("Arejais radius: "))
summa = 0

if r1<=r2:
    print("Nav rinkis!")
    exit()

for x in range(1,int(r1.quantize(Decimal("1."), rounding=ROUND_UP))):
    y = r1 * Decimal(1-(Decimal(x/r1)**2)).sqrt()
    summa += int(y.quantize(Decimal("1."), rounding=ROUND_DOWN))

for x in range(1,int(r2.quantize(Decimal("1."), rounding=ROUND_DOWN)+1)):
    y = r2 * Decimal(1-(Decimal(x/r2)**2)).sqrt()
    summa -= int(y.quantize(Decimal("1."), rounding=ROUND_DOWN))

print(summa*4)