num1=(int(input("Enter First 2 Digit Number: ")))
num2=(int(input("Enter Second 2 Digit Number: ")))
left1=(int(num1//10))
right1=(int(num1%10))
left2=(int(num2//10))
right2=(int(num2%10))
print ("Merged Number: ""{}{}{}{}".format(left1,left2,right1,right2))
