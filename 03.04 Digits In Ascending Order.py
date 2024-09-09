num= (int(input("Enter A Number: ")))
a=num//100
bb=num%100
b=bb//10
c=num%10
if a<b and b<c:
    print ("YES")
else:
    print ("NO")