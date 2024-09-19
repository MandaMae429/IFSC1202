n=int(input("Enter Start of Range: "))
m=int(input("Enter End of Range: "))
print("Prime Numbers between",n,"and", m)
for x in range(n,m+1):
  isprime=True
  for y in range(2,(x//2)+1):
    if x%y==0:
      isprime=False
      continue
  if isprime:
    print(x)
