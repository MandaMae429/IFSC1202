n=(int(input("Enter Number: ")))
fact=1
if n >= 1:
    for x in range (1, n+1):
        fact=fact*x
print (fact)