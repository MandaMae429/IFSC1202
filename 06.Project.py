outputfile=open("06.Project Output File.txt", "w")
inputfile=open("06.Project Input File.txt", "r")
inct=0
mgct=0
otct=0
line=inputfile.readline()
while True:
    print(repr(line))
    if not line:
        break
    elif line==('**Insert Merge File Here**\n'):
        mergefile=open("06.Project Merge File.txt")
        merge=mergefile.readline()
        while True:
            if not merge:
                outputfile.write("\n") 
                break
            mgct+=1
            otct+=1
            outputfile.write(merge)
            merge=mergefile.readline()   
    else: 
        inct+=1
        otct+=1
        outputfile.write(line)
    line=inputfile.readline()
print ("{} input file records\n{} merge file records\n{} output file records".format(inct, mgct, otct))
