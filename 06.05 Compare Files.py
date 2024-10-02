fa=open("06.05 CompareFileA.txt")
fb=open("06.05 CompareFileB.txt")
line=0
count=0
linea=fa.readline()
lineb=fb.readline()
while True:
    line+=1
    if not linea and not lineb:
        break
    elif linea!=lineb:
        count+=1
        print ("Line: {} -File A: {}".format(line,linea))
        print ("Line: {} -File B: {}".format(line,lineb))
    linea=fa.readline()
    lineb=fb.readline()
print("{} differences".format(count))