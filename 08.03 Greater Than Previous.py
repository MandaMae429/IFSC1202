#Prompt for a string containing integers separated by spaces.
myinput=input("Enter Values Separated by Spaces: ")
#Load the values into a list.
mylist=myinput.split()
#Print all of the elements that are greater than the previous element.
for x in range(len(mylist)):
    y=x-1
    if mylist[x] > mylist[y]:
        print (mylist[x])