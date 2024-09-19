n=int(input("Enter Start of Range: "))
m=int(input("Enter End of Range: "))
for x in range(n,m+1):
  i=x
  digits=0
  while i>0:
    if i<10:
      digits+=1
      i=0
    else:
      i=i//10
      digits+=1
  sum=0
  i = x
  for y in range(digits):
    sum+=(i%10)**digits
    i=i//10
  if sum==x:
    print(x)
