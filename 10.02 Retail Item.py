#Create a class called RetailItem that holds data about an Item in a retail store.
#The class should have the following attributes:
#Description - description of the item (default "")
#UnitsOnHand - the number of units in inventory (default 0)
#Price - the item's retail price (default 0)
class RetailItem ():
    def __init__(self, description, unitsonhand=0, price=0):
          
#Create a constructor that accepts the Description, UnitOnHand, and Price, then sets them to attributes in the RetailItem Class.
        self.Description=description
        self.UnitsOnHand=unitsonhand
        self.Price=price 
#If one of the attributes is not present, then set the attribute to the default value.
      
#Create a method called InventoryValue, which returns the UnitsOnHand times Price.
    def InventoryValue(self):
        inventoryvalue= self.UnitsOnHand * self.Price
        return inventoryvalue

#Read the 10.02 Inventory.txt file and creates three objects, one for each item.
file=open("10.02 Inventory.txt", "r")
file.readline()
#Display a report that displays the Description, Units On Hand, Price, and Inventory Value