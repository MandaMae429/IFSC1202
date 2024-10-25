#Prompt for a string containing integers separated by spaces.
myinput=input("Enter Values Separated by Spaces: ")
#Load the values into a list.
mylist=myinput.split()
#Determine and print the quantity of elements that are greater than both of their neighbors.
for x in range(len(mylist)):
    y=x-1
    z=x+1
    count=0
    if mylist[x] > mylist[y] and mylist[x]>mylist[z]:
        count=1
        continue
#NOT FINISHED
#The first and the last items of the list shouldn't be considered because they don't have two neighbors.