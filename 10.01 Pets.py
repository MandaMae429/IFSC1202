#Create a class called Pet which has the following attributes:
#Name - name of pet
#Type - type of pet, such as "Cat", "Dog", etc
#Age - age of pet
class Pets ():
     def __init__(self, name, type, age):
#The constructor for the Pet class should not have any arguments.
        self.Name=name
        self.Type=type
        self.Age=age
#Read the 10.01 Pets.txt file, create three pet objects, one for each line, and print the object attributes for the pets using the .format 
file=open("10.01 Pets.txt", "r")
print (file.readline())

#print (file.readline())
#Print the Name, Type, and Age attributes from each of the pet objects