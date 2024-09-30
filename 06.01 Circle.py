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

output=("{:>20}{:>20}{:>20}{:>20}\n".format("Radius","Diameter","Circumference","Area"))
while x!='':
    trim=x.find('\n')

    r=float(x)
    diam=diameter(r)
    circ=circumference(r)
    are=area(r)
    output=output+("{:>20n}{:>20n}{:>20n}{:>20n}\n".format(r,diam,circ,are))

    print (output)
