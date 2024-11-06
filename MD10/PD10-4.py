for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            for d in range(1,10):
                if (a!=b) and (a!=c) and (a!=d) and (c!=b) and (d!=b) and (c!=d) and (10*(a+c)+b+d == a*b*c*d):
                    print(f"{a}{b}{c}{d}")