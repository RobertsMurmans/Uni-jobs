while True:
    try:
        start = float(input(">Viens galapunkts = "))
    except:
        print(">Neparieza ievade")
    else:
        break

while True:
    try:
        beigas = float(input(">Otrs galapunkts = "))
    except:
        print(">Neparieza ievade")
    else:
        break

if start > beigas:
    start, beigas = beigas, start

while True:
    try:
        a = float(input(">A = "))
    except:
        print(">Neparieza ievade")
    else:
        break

while True:
    try:
        b = float(input(">B = "))
    except:
        print(">Neparieza ievade")
    else:
        break

while True:
    try:
        c = float(input(">C = "))
    except:
        print(">Neparieza ievade")
    else:
        break

while True:
    try:
        d = float(input(">D = "))
    except:
        print(">Neparieza ievade")
    else:
        break

while True:
    try:
        prec = float(input(">Precizitate = "))
    except:
        print(">Neparieza ievade")
    else:
        break

n = 10
delta = beigas-start / n
s1=0

for x in range(start*n/delta, beigas*n/delta, n):
    dx = x*delta*delta/n
    Fx = a*dx*dx*dx+b*x*x+c+d
    s1 = s1+Fx

while True:
    s2=s1
    s1=0
    n=n*2
    delta = beigas-start / n

    for x in range(start*n/delta, beigas*n/delta, delta):
        dx = x*delta*delta/n
        Fx = a*dx*dx*dx+b*x*x+c+d
        s1 = s1+Fx
    if abs(s1-s2) < prec:
        break

print("Laukms zem grafika =", s1)