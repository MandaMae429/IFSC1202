n=int(input("Enter Fibonnaci Sequence Number: "))
res=0
a=0
b=1
count=0
while count<=n:
  if count<2:
    res=count
  else:
    res=a+b
  count+=1
  a=b
  b=res
print(res)