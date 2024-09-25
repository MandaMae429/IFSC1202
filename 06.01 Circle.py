import math
def diameter(r):
    return (r*2)
def circumference(r):
    return (r*math.pi*2)
def area(r):
    return (math.pi*r*r)

radiustextfile=open ("06.01 Radius.txt", "r")
x=radiustextfile.readline()
print (x)
radiustextfile.close()