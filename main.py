path = "C:\\Users\\Fark\\Desktop\\NonSus.txt"

def times1024(inp):
    out = ""
    for i in range(1024):
        out = out+inp
    return out

def times32(inp):
    out = ""
    for i in range(32):
        out = out+inp
    return out

Abyte = "A"

AkB = times1024(Abyte)

AMB = times1024(AkB)

AGB = times1024(AMB)

payload = times32(AGB)

file = open(path, "w")

file.write(payload)

file.close()
