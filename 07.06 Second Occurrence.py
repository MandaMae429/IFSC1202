secd=input("Enter a string: ")
f=secd.count("f")
if f==2:
    print (secd.rfind("f"))
elif f==1:
    print ("One f")
else:
    print ("Zero f")