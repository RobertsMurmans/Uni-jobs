def kapinat(baze, kapinatajs):
    if kapinatajs == 0:
        return 1
    elif kapinatajs < 0:
        return 1 / kapinat(baze, -kapinatajs)
    elif kapinatajs % 2 == 0:
        pus_kapinatajs = kapinat(baze, kapinatajs // 2)
        return pus_kapinatajs * pus_kapinatajs  
    else:
        return baze * kapinat(baze, kapinatajs - 1)
    
armstrongs = 0

def sort(string):
    rezult = string[0]
    for element in string[1:]:
        for i in range(len(rezult)):
            if int(element) > int(rezult[i]):
                rezult = rezult[0:i] + element + rezult[i:]
                break
        else:
            rezult = rezult + element
    return rezult


def cikls(start, index, summa, cipars, pakape):
    if index == 0:
        if sort(str(summa)) == cipars:
            global armstrongs
            if armstrongs < summa:
                armstrongs = summa
            return 
        return 
    for i in range(start, -1, -1):
        cikls(i, index-1, summa+kapinat(i,pakape), cipars+str(i), pakape)

digits = 7

while True:

    for i in range(9,0,-1):
        cikls(i,digits-1,kapinat(i,digits),str(i), digits)
    
    print(f"{digits} digit number calulated, largest one found so far is: {armstrongs}.")
    if (input("Do you want to continue? ")[0] != "y"):
        break
    digits+=1

print(armstrongs)

