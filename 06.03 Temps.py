def FahrToCel(f):
    return ((f - 32) * 5 / 9)
ftemp=open("06.03 FTemps.txt", "r")
ctemp=open("06.03 Ctemps.txt", "w")
fread=ftemp.readline()
while True:
    if not fread:
        break
    ctemp.write("{:<5.1f}\n".format(FahrToCel(float(fread))))
    #print(FahrToCel(float(fread)))
    fread=ftemp.readline()
ctemp.close()
with open ("06.03 Ctemps.txt", "r") as f:
    for line in f:
        print(line, end="")