i=True
count=0
max =0
while i:
  n=input("Enter a Number (CR to Quit)")
  if n!='':
    if max<int(n):
        max=int(n)
        count+=1
    else:
        count+=1
  else:
    if count==0:
      print ("Sequence Length is 0")
      break
    else:
      print ("Maximum: ", max)
      break
