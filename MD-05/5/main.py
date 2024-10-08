x_in = float(input("x: "))
y_in = float(input("y: "))

def findGoldenSpiral2(x,y,a,b,xr,yu,xl,yd,t,t2):
    while True:
        if xl <= x <= xr and yd <= y <= yu:
            if x > 0:
                if y > 0:
                    return min(a,b)
                else:
                    return min(a,b)
            else:
                if y > 0:
                    return min(a,b)
                else:
                    return min(a,b)
                
        if a >= b:
            if t == 1:
                xr = xr + a
                t=0
            else:
                xl = xl - a
                t=1
            b = b + a
        else:
            if t2 == 1:
                yu = yu + b
                t2=0
            else:
                yd = yd - b
                t2=1
            a = a + b

a,b,xr,yu,xl,yd,t,t2 = 1,1,1,1,0,0,1,1
fib1, fib2 = None, None
while True:
    if xl <= x <= xr and yd <= y <= yu:
        if x > 0:
            if y > 0:
                if float(xr) == x or float(yu) == y:
                    if float(xr) == x and float(yu) == y:
                        fib1 = findGoldenSpiral2(x+1, y,a,b,xr,yu,xl,yd,t,t2)
                        fib2 = findGoldenSpiral2(x, y+1,a,b,xr,yu,xl,yd,t,t2)
                        if fib1 > fib2:
                            fib1,fib2=fib2,fib1
                    elif float(xr) == x: 
                        fib1 = findGoldenSpiral2(x+1, y,a,b,xr,yu,xl,yd,t,t2)
                    elif float(yu) == y:
                        fib1 = findGoldenSpiral2(x, y+1,a,b,xr,yu,xl,yd,t,t2)
            else:
                if float(xr) == x or float(yd) == y:
                    if float(xr) == x and float(yu) == y:
                        fib1 = findGoldenSpiral2(x+1, y,a,b,xr,yu,xl,yd,t,t2)
                        fib2 = findGoldenSpiral2(x, y-1,a,b,xr,yu,xl,yd,t,t2)
                        if fib1 > fib2:
                            fib1,fib2=fib2,fib1
                    elif float(xr) == x: 
                        fib1 = findGoldenSpiral2(x+1, y,a,b,xr,yu,xl,yd,t,t2)
                    elif float(yd) == y:
                        fib1 = findGoldenSpiral2(x, y-1,a,b,xr,yu,xl,yd,t,t2)
        else:
            if y > 0:
                if float(xl) == x or float(yu) == y:
                    if float(xl) == x and float(yu) == y:
                        fib1 = findGoldenSpiral2(x-1, y,a,b,xr,yu,xl,yd,t,t2)
                        fib2 = findGoldenSpiral2(x, y+1,a,b,xr,yu,xl,yd,t,t2)
                        if fib1 > fib2:
                            fib1,fib2=fib2,fib1
                    elif float(xl) == x: 
                        fib1 = findGoldenSpiral2(x-1, y,a,b,xr,yu,xl,yd,t,t2)
                    elif float(yu) == y:
                        fib1 = findGoldenSpiral2(x, y+1,a,b,xr,yu,xl,yd,t,t2)
            else:
                if float(xl) == x or float(yd) == y:
                    if float(xl) == x and float(yu) == y:
                        fib1 = findGoldenSpiral2(x-1, y,a,b,xr,yu,xl,yd,t,t2)
                        fib2 = findGoldenSpiral2(x, y-1,a,b,xr,yu,xl,yd,t,t2)
                        if fib1 > fib2:
                            fib1,fib2=fib2,fib1
                    elif float(xl) == x: 
                        fib1 = findGoldenSpiral2(x-1, y,a,b,xr,yu,xl,yd,t,t2)
                    elif float(yd) == y:
                        fib1 = findGoldenSpiral2(x, y-1,a,b,xr,yu,xl,yd,t,t2)
        a,b,c = min(a,b), fib1, fib2
        break
            
    if a >= b:
        if t == 1:
            xr = xr + a
            t=0
        else:
            xl = xl - a
            t=1
        b = b + a
    else:
        if t2 == 1:
            yu = yu + b
            t2=0
        else:
            yd = yd - b
            t2=1
        a = a + b

print(a)

if b != None:
    print(b)

if c != None:
    print(c)
    

input()
