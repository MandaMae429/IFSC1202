n=int(input("enter N:"))
for x in range(1,n+1):
  out=str(1)
  for y in range(2,x+1):
    out=out+str(y)
  print (out)
