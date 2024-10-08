x_in = float(input("x: "))
y_in = float(input("y: "))

def findGoldenSpiral(x,y):
    a,b,xr,yu,xl,yd,t,t2 = 1,1,1,1,0,0,1,1
    while True:
        if xl <= x <= xr and yd <= y <= yu:
            if x > 0:
                if y > 0:
                    return xr,yu,min(a,b)
                else:
                    return xr,yd,min(a,b)
            else:
                if y > 0:
                    return xl,yu,min(a,b)
                else:
                    return xl,yd,min(a,b)
                
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

x_test, y_test, fib_min = findGoldenSpiral(x_in, y_in)

if float(x_test) == x_in or float(y_test) == y_in:
    if float(x_test) == x_in and float(y_test) == y_in:
        if x_in > 0:
            if y_in > 0:
               z, z, fib1 = findGoldenSpiral(x_in+1, y_in)
               z, z, fib2 = findGoldenSpiral(x_in, y_in+1)
            else:
               z, z, fib1 = findGoldenSpiral(x_in+1, y_in)
               z, z, fib2 = findGoldenSpiral(x_in, y_in-1)
        else:
            if y_in > 0:
               z, z, fib1 = findGoldenSpiral(x_in-1, y_in)
               z, z, fib2 = findGoldenSpiral(x_in, y_in+1)
            else:
               z, z, fib1 = findGoldenSpiral(x_in-1, y_in)
               z, z, fib2 = findGoldenSpiral(x_in, y_in-1)

        print(fib_min, fib1, fib2)
    elif float(x_test) == x_in:
        if x_in > 0:
            z, z, fib1 = findGoldenSpiral(x_in+1, y_in)
        else:
            z, z, fib1 = findGoldenSpiral(x_in-1, y_in)

        print(fib_min, fib1)
    elif float(y_test) == y_in:
        if y_in > 0:
            z, z, fib1 = findGoldenSpiral(x_in, y_in+1)
        else:
            z, z, fib1 = findGoldenSpiral(x_in, y_in-1)

        print(fib_min, fib1)

else:
    print(fib_min)
