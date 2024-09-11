num1=float(input("Enter First Number: "))
oper=input("Enter Operator: ")
num2=float(input("Enter Second Number: "))
if oper=="+" or oper=="-" or oper=="*" or oper=="/":
    if oper=="+":
        output=num1+num2
    elif oper=="-":
        output=num1-num2
    elif oper=="*":
        output=num1*num2
    else:
        output=num1/num2
    print (num1,oper,num2,"=",output)
else:
    print ("Invalid Operator")
