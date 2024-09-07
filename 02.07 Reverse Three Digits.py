#Enter a 3 Digit Number: 291
#Reverse of Digits: 192


#Enter a 3 Digit Number: 321
#Reverse of Digits: 123


#Enter a 3 Digit Number: 444
#Reverse of Digits: 444
num=(int(input("Enter a 3 Digit Number: ")))
num1=num%10
num2=num%100
num22=num2//10
num3=num//100
#print (num22)
print("Reverse of Digits: ""{}{}{}".format(num1,num22,num3))
