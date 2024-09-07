num=(int(input("Enter a 3 Digit Number: ")))
a=num//100
b=num//10
b2=b%10
c=num%10
sum=a+b2+c
print ("Sum of Digits: ""{}".format(sum))