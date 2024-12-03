class Student:
  def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores
  def RunningAverage(self):
    rtotal = 0
    count = 0
    for grade in self.Grades:
      if grade != "":
        count += 1
        rtotal += int(grade)
    if count == 0:
      return 0
    return rtotal / count

  def TotalAverage(self):
    total=0
    for grade in self.Grades:
      if grade == "":
        total+=0
      else:
        total+=int(grade)
    if len(self.Grades) == 0:
      return 0
    return total / len(self.Grades)

  def LetterGrade(self):
      tavg = self.TotalAverage()
      match (tavg):
        case _ if tavg >= 90:
          return "A"
        case _ if tavg >= 80:
          return "B"
        case _ if tavg >= 70:
          return "C"
        case _ if tavg >= 60:
          return "D"
        case _ if tavg < 60:
          return "F"

#Main
f = open("10.Project Student Scores.txt")
list=[]
#print(line)
for line in f:
  line=line.split(",")
  scores=[]
  for x in range(len(line)):
    line[x]=line[x].strip()
  for x in range(3,len(line)):
    scores.append(line[x])
  list.append(Student(line[0],line[1],line[2],scores))
spacer = "-"*12
print("{:>12} {:>12} {:>12} {:>12} {:>12} {:>12}".format("First", "Last", "ID", "Running", "Semester", "Letter"))
print("{:>12} {:>12} {:>12}{:>12} {:>12} {:>12}".format("Name","Name","Number","Average","Average","Grade"))
print("{:12} {:12} {:12} {:12} {:12} {:12}".format(spacer,spacer,spacer,spacer,spacer,spacer))
for items in list:
  print("{:>12} {:>12} {:>12} {:>12.2f} {:>12.2f} {:>12}".format(items.FirstName,items.LastName,items.TNumber,items.RunningAverage(),items.TotalAverage(),items.LetterGrade()))