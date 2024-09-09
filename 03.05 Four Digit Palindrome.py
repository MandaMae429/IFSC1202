num= (int(input("Enter A Number: ")))
thou =num//1000
hu=num//100
hun=hu%10
te=num%100
ten=te//10
one=num%10
#print (thou, hun, ten, one)
if thou==one and hun==ten:
    print ("YES")
else:
    print ("NO")