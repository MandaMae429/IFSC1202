# Step 1 - Define the class object "Ball"
from math import pi
class Ball ():
     def __init__(self, balltype, diameter, pressure):

# Step 2 - Define the initializer and any default values
        def __init__(self, balltype="Basketball", diameter=9.51, pressure=8.0):
# Step 3 - Define the object attributes
            self.BallType = balltype
            self.Diameter = diameter
            self.Pressure = pressure
        def Circumference(self):
            circumference=math.pi*self.Diameter
            return 
# Step 4 - Here is another action        
        def ChangePressure(self, pressurechange):
            self.Pressure+=pressurechange
            return self.Pressure


# Step 5 - Create 4 instances of ball
myball1 = Ball("Basketball", 9.51, 8.0)
myball2 = Ball("Volleyball", 8.15, 7.5)
myball3 = Ball("Soccerball", 8.65, 9.0)
myball4 = Ball()

# Print the attributes
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())
print (myball2.BallType, myball2.Diameter, myball2.Pressure, myball2.Circumference())
print (myball3.BallType, myball3.Diameter, myball3.Pressure, myball3.Circumference())
print (myball4.BallType, myball4.Diameter, myball4.Pressure, myball4.Circumference())

# Change the Diameter attribute of myball1
myball1.Diameter = 9.0
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())

# Add Pressure to myball1
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
newpressure = myball1.ChangePressure(1)
print (newpressure)
print (myball1.BallType, myball1.Diameter, myball1.Pressure, myball1.Circumference())