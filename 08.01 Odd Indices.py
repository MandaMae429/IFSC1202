n=input("Enter Values Seperated by Spaces: ")
list=n.split()
for i in range(len(list)):
    if i%2==1:
        print (list[i])
