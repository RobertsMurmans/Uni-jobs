skaitlis = int(input("Ievadiet naturalu skaitli no 1 lidz 999: "))

if 999 < skaitlis or skaitlis < 1:
    print("ND")
    exit()

vieni   = skaitlis % 10
desmiti = (skaitlis // 10) % 10
simti   = skaitlis // 100

print(simti, desmiti, vieni)

match simti:
    case 1:
        print("simts", end=" ")
    case 2:
        print("divi simti", end=" ")
    case 3:
        print("triss simti", end=" ")
    case 4:
        print("cetri simti", end=" ")
    case 5:
        print("pieci simti", end=" ")
    case 6:
        print("sesi simti", end=" ")
    case 7:
        print("septini simti", end=" ")
    case 8:
        print("astoni simti", end=" ")
    case 9:
        print("devini simti", end=" ")
    case _:
        pass

if desmiti == 1:
    match vieni:
        case 1:
            print("vienpadsmit", end=" ")
        case 2:
            print("divpadsmit", end=" ")
        case 3:
            print("trispadsmit", end=" ")
        case 4:
            print("cetripadsmit", end=" ")
        case 5:
            print("piecpadsmit", end=" ")
        case 6:
            print("sespadsmit", end=" ")
        case 7:
            print("septinpadsmit", end=" ")
        case 8:
            print("astonpadsmit", end=" ")
        case 9:
            print("sevinpadsmit", end=" ")
        case _:
            pass

else:
    match desmiti:
        case 2:
            print("divdesmit", end=" ")
        case 3:
            print("trisdesmit", end=" ")
        case 4:
            print("cetridesmit", end=" ")
        case 5:
            print("piecdesmit", end=" ")
        case 6:
            print("sesdesmit", end=" ")
        case 7:
            print("septindesmit", end=" ")
        case 8:
            print("astondesmit", end=" ")
        case 9:
            print("devindesmit", end=" ")
        case _:
            pass

    
    match vieni:
        case 1:
            print("viens", end=" ")
        case 2:
            print("divi", end=" ")
        case 3:
            print("tris", end=" ")
        case 4:
            print("cetri", end=" ")
        case 5:
            print("pieci", end=" ")
        case 6:
            print("sesi", end=" ")
        case 7:
            print("septini", end=" ")
        case 8:
            print("astoni", end=" ")
        case 9:
            print("devini", end=" ")
        case _:
            pass
        

