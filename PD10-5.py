from decimal import *
getcontext().prec = 5

r = Decimal(input("Radius: "))

if r < Decimal(2).sqrt():
    print("Rinkis par mazu lai butu pat viens!")
    exit()

for x in range(1,int(r.quantize(Decimal("1."), rounding=ROUND_UP))):
    print(x)