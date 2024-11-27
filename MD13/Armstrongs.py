def tabula(cipars):
    match cipars:
        case "0":
            return 0
        case "1":
            return 1
        case "2":
            return divi
        case "3":
            return triss
        case "4":
            return cetri
        case "5":
            return pieci
        case "6":
            return sesi
        case "7":
            return septini
        case "8":
            return astoni
        case "9":
            return devini
    return 0


def pakape(baze, kapinatajs):
    rezultats = 1
    for n in range(kapinatajs):
        rezultats = rezultats*baze
    return rezultats
    

def summa(skaitlis):
    summa = 0
    for cipars in str(skaitlis):
        summa = summa + tabula(cipars)
        if summa > skaitlis:
            return 0
    return summa == skaitlis
    

#=======================================================================#

armstrongs = ""
cipari = 5

while True:
    divi = pakape(2,cipari)
    triss = pakape(3,cipari)
    cetri = pakape(4,cipari)
    pieci = pakape(5,cipari)
    sesi = pakape(6,cipari)
    septini = pakape(7,cipari)
    astoni = pakape(8,cipari)
    devini = pakape(9,cipari)

    maksimums = pakape(10, cipari)
    minimums = pakape(10, cipari-1)

    x = minimums
    while x < maksimums:
        if summa(x):
            armstrongs = str(x)
        x += 1
     
    print(f"Aprekinats {cipari} ciparu gars skaitlis, lielakais lidz sim atrastais armstronga skaitlis ir: {armstrongs}.")

    if input("Turpinat(y/n)? ")[0] == "y":
        cipari += 1
    else: 
        break

print(f"Lielakais atrastais armstronga skaitlis ir: {armstrongs}")
