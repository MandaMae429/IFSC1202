i=True
sum=0
count =0
while i:
  n=input("Enter a Number (CR to Quit)")
  if n!='':
    sum+=int(n)
    count+=1 #count=count+1
  elif count==0:
    print ("Sequence Length is 0")
    break
  else:
    print ("Average: ",sum/count)
    break    