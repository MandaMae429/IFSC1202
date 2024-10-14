whrf=input("Enter a string: ")
f=whrf.count("f")
if f ==1:
    print(whrf.find("f"))
elif f==2:
    print(whrf.find("f"), whrf.rfind("f"))
else:
    print("0")
