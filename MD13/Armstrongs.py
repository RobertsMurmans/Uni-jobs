def pakape(baze, kapinatajs):
    rezultats = 1
    for n in range(kapinatajs):
        rezultats = rezultats*baze
    return rezultats

def summa(skaitlis, cipari):
    summa = 0
    for cipars in str(skaitlis):
        summa = summa+pakape(int(cipars),cipari)
    return summa


def main():
    armstrongs = ""
    cipari = 3

    while True:
        maksimums = pakape(10,cipari)
        minimums = pakape(10, cipari-1)

        for x in range(minimums,maksimums):
            if summa(x, cipari) == x:
                armstrongs = str(x)
        
        print(f"Aprekinats {cipari} ciparu gars skaitlis, lielakais, lidz sim atrastais armstronga skaitlis ir: {armstrongs}")

        if input("Turpinat(y/n)?")[0] == "y":
            cipari += 1
        else: 
            break

    print(armstrongs)

    
if __name__ == "__main__":
    main()

