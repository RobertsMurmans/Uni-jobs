virkne = input("Ievade >> ")
garums = len(virkne)

for index in range(garums):
    print(virkne[index:],end="")
    print(virkne[:index])
 