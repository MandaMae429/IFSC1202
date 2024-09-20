n=int(input("Enter N:"))
sum=0
res=1
for x in range(1,n+1):
  res*=x
  sum+=res
print(sum)