import math
a=float((input("Enter Side 1: ")))
b=float((input("Enter Side 2: ")))
c=float((input("Enter Side 3: ")))
s=(a+b+c)/2
heb=(s*(s-a)*(s-b)*(s-c))
print (math.sqrt (heb))