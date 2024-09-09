#Enter Point A: 10
#Enter Point B: 35
#Enter Point C: 30
#20


#Enter Point A: 35
#Enter Point B: 10
#Enter Point C: 30
#5


#Enter Point A: 100
#Enter Point B: 151
#Enter Point C: 149
#49

a=int(input("Enter Point A: "))
b=int(input("Enter Point B: "))
c=int(input("Enter Point C: "))
dif1=(b-a)
dif2=(c-a)
#print (dif1)
#print (dif2)

if dif1<dif2 and dif1 >= 0:
    print (dif1)
elif  dif2<dif1 and dif2 >= 0:
    print (dif2)
else:
    print