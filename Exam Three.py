import math

class Triangle:
  def __init__(self, s1, s2, s3):
    self.s1 = s1
    self.s2 = s2
    self.s3 = s3
  def type(self):
    if self.s1 == self.s2 == self.s3:
      return "Equilateral"
    elif self.s1 == self.s2 or self.s1 == self.s3 or self.s2 == self.s3:
      return "Isoceles"
    else:
      return "Scalene"
  def perimeter(self):
    return self.s1 + self.s2 + self.s3
  def area(self):
    s= (self.s1 + self.s2 + self.s3) / 2
    return (s*(s-self.s1)*(s - self.s2)*(s - self.s3))**(1/2)
  def angles(self):
    a3 = math.degrees(math.acos(((self.s1**2)+(self.s2**2)-(self.s3**2))/(2*self.s1*self.s2)))
    a1 = math.degrees(math.acos(((self.s2**2)+(self.s3**2)-(self.s1**2))/(2*self.s2*self.s3)))
    a2 =180-(a1+a3)
    return [a1,a2,a3]

#Main
f = open("Exam Three Triangles.txt")
TriangleList=[]
for line in f:
  line=line.split(",")
  mytri = Triangle(float(line[0]),float(line[1]),float(line[2]))
  TriangleList.append(mytri)
f.close()
print("{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}{:>12}".format("Type","Side 1","Side 2","Side 3","Area","Perimeter","Angle 1","Angle 2","Angle 3"))
for tri in TriangleList:
  print("{:>12}{:>12.3f}{:>12.3f}{:>12.3f}{:>12.3f}{:>12.3f}{:>12.3f}{:>12.3f}{:>12.3f}".format(tri.type(),tri.s1,tri.s2,tri.s3,tri.area(),tri.perimeter(),tri.angles()[0],tri.angles()[1],tri.angles()[2]))

