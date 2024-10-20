#Prompt for a string containing integers separated by spaces.
myinput=input("Enter Values Seperated by Spaces: ")
#Load the values into a list.
mylist=myinput.split()
#Print the values that are odd.
for x in range(len(mylist)):
        mynum=int(mylist[x])
        if mynum %2==1:
            print(mynum)

#Do not use the list or string functions or methods for this assignment (except the .split() method).
#Do not use the for x in y iterator; use for x in range(n)
