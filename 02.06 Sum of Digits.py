num=(int(input("Enter a 3 Digit Number: ")))
a=num//100
#print (a)
b=num//10
b2=b%10
#print (int(b2))
c=num%10
#print (c)
sum=a+b2+c
print ("Sum of Digits: ""{}".format(sum))