one=(int(input("Enter First Number: ")))
two=(int(input("Enter Second Number: ")))
thr=(int(input("Enter Third Number: ")))
#if one<=two and one<=thr:
    #print (one)
#elif two<=one and two<=thr:
    #print (two)
if one > two:
    one,two = two,one
elif one > thr:
    one,thr = thr,one
elif two > thr:
    two,thr = thr,two
    
print (one, two, thr)