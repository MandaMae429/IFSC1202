#Prompt for a string containing integers separated by spaces.
myinput=input("Enter Values Separated by Spaces: ")
#Load the values into a list.
mylist=myinput.split()
#Determine the element in the list with the largest value.
#Print the value of the largest element and then the index number.
#If the largest element is not unique, print the index of the first instance.