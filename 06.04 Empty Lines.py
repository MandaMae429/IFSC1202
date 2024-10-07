emptylinestext=open ("06.04 EmptyLinesInput.txt", "r")
emptylineoutput=open("06.04 EmptyLinesOutput.txt", "w")
count=0
total=0
line=emptylinestext.readline()
while True:
    #print(repr(line))
    if not line:
        break
    elif line==' \n':
        total+=1
    else:
        total+=1
        count+=1
        emptylineoutput.write("{}".format(line))
    line=emptylinestext.readline()    
print("{}Records Read\n{}Records Written".format(total,count))
emptylinestext.close()