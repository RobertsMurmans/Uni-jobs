def pakape(baze, kapinatajs):
    rezultats = 1
    for n in range(kapinatajs):
        rezultats = rezultats*baze
    return rezultats


def summa(skaitlis, cipari):
    summa = 0
    deviniVertiba = pakape(9,cipari)
    maxSumma = deviniVertiba*cipari
    
    for cipars in str(skaitlis):
        summa = summa + pakape(int(cipars), cipari)
        maxSumma = maxSumma + maxSumma - deviniVertiba
        if summa > skaitlis > maxSumma:
            return 0
    return summa == skaitlis


def main():
    armstrongs = ""
    cipari = 3

    while True:
        maksimums = pakape(10, cipari)
        minimums = pakape(10, cipari-1)

        x = minimums
        while x < maksimums:
            if summa(x, cipari):
                armstrongs = str(x)
            x += 1
        
        print(f"Aprekinats {cipari} ciparu gars skaitlis, lielakais lidz sim atrastais armstronga skaitlis ir: {armstrongs}.")

        if input("Turpinat(y/n)?")[0] == "y":
            cipari += 1
        else: 
            break

    print(f"Lielakais atrastais armstronga skaitlis ir: {armstrongs}")
    

if __name__ == "__main__":
    main()

