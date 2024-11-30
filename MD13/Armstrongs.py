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
        case "m":
            return mx
    return -1


def pakape(baze, kapinatajs):
    rezultats = 1
    for n in range(kapinatajs):
        rezultats = rezultats*baze
    return rezultats
    

def summa(skaitlis):
    summa = 0
    maxSum = tabula("m")
    for cipars in str(skaitlis):
        summa = summa + tabula(cipars)
        maxSum = maxSum - tabula("9") + tabula(cipars)
        if summa > skaitlis or skaitlis > maxSum:
            return 0
    return 1

#=======================================
armstrongs = ""
cipari = 5

while True:
    x = pakape(10, cipari)
    minimums = pakape(10, cipari-1)
    divi = pakape(2,cipari)
    triss = pakape(3,cipari)
    cetri = divi*divi
    pieci = pakape(5,cipari)
    sesi = triss*divi
    septini = pakape(7,cipari)
    astoni = cetri*divi
    devini = triss*triss
    mx = devini*cipari
    while x > minimums:
        if summa(x):
            armstrongs = str(x)
            break
        x -= 1

    print(f"Aprekinats {cipari} ciparu gars skaitlis, lielakais lidz sim atrastais armstronga skaitlis ir: {armstrongs}.")

    if input("Turpinat(y/n)? ")[0] == "y":
        cipari += 1
    else: 
        break

print(f"Lielakais atrastais armstronga skaitlis ir: {armstrongs}")
