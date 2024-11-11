def cityfix(city):
  city=city.lower()
  city=city.capitalize()
  return city

def citycheck(city,list):
  if city in list:
    return True
  else:
    return False
def distance(city1,city2,table):
  x=table[0].index(city1)
  #print(x)
  y=table[0].index(city2)
  #print(y)
  #print(table[x][y])
  return table[x][y]
#open file and create lists
citytable=open("09.Project Distances.csv")
line = citytable.readline()
#print(line)
table=[]
while True:
  if not line:
    break
  temp=line.strip()
  #print(temp)
  table.append(temp.split(","))
  line=citytable.readline()
citytable.close()
y=0
for x in range(len(table)):
  for y in range(len(table[x])):
    print("{:10}".format(table[x][y]),end="")
  print()

citylist=[]
for x in range(1,len(table[0])):
  citylist.append(table[0][x])
#print(citylist)
#print(table)
x=0
while True:
  fromc=input("Enter From City: ")
  fromc=cityfix(fromc)
  leave=False
  for x in range(1,len(table[0])):
    if fromc==table[0][x]:
      leave=True
      print(x)
      break
  if leave:
    break
  else:
    print("Invalid From City")
y=0
while True:
  toc=input("Enter To City: ")
  toc=cityfix(toc)
  leave=False
  for y in range(1,len(table[0])):
    if toc==table[y][0]:
      leave=True
      print(x)
      break
  if leave:
    break
  else:
    print("Invalid To City")

print("{} to {} - {} miles".format(fromc,toc,table[y][x]))


