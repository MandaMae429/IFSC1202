def namefix(name):
  name=name.lower()
  name=name.strip()
  name=name.capitalize()
  return name

def namesearch(name,list):
  count =1
  for names in list:
    found= False
    #print(names, name)
    if name==names:
      return count
    else:
      count+=1
  return 0
#open file and create lists
names = open("Names.txt")
boys=[]
girls=[]
#input file to lists
while True:
  line= names.readline()
  if not line:
    break
  line=line.strip()
  temp=line.split(", ")
  boys.append(temp[0])
  girls.append(temp[1])
  #Check strip
  #print(temp)
#Check Split lists
#print(boys,girls)
#Close file
names.close()

#get input and fix
namein=input("Enter a Name: ")
namein=namefix(namein)
#check for exit condition, otherwise loop
while namein != "Q":
  # check lists for name and print rank or not found
  #print(namesearch(namein,boys))
  if namesearch(namein,boys)>0:
    print("Boy's Name - Rank:",namesearch(namein,boys))
  elif namesearch(namein,girls)>0:
    print("Girl's Name - Rank:",namesearch(namein,girls))
  else:
    print("Name Not Found")
  namein=input("Enter a Name: ")
  namein=namefix(namein)