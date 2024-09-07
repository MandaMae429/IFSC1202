a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if a == b and b == c:
    print ("3")
elif b != a and b == c or c==a:
    print("2")
elif c != a and c != b:
    print ("0")
else:
    print