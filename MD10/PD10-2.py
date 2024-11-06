virkne = input("Ievade >> ")
garums = len(virkne)

for x in range(garums):
    for i in range(x, x+garums):
        index = i % garums
        print(virkne[index],end="")
    print()
    
