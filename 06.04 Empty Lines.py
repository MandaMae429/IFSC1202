emptylinestext=open ("06.04 EmptyLinesInput.txt", "r")
count=0
total=0
x=emptylinestext.readline()
while True:
    line=x
    if not line:
        break
    elif time=='\n':
        total=+1
        continue
    else:
        total+=1
        count+=1
        print (line.rstrip())
    print("Total:{} Count:{}".format(total,count))
emptylinestext.close()