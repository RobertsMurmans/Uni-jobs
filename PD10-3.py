beigas = int(input("Beigu skaitlis (lielaka par 1): "))

if beigas < 2:
    print("Nederiga ieavade!")
    exit()

for x in range(2,beigas+1):
    for y in range(2,x):
        if x%y==0:
            break
    else:#Var ari ar variablu (irPirmskaitlis) un break vieta ielikt (irPirmskaitlis = 0)
        print(x)
