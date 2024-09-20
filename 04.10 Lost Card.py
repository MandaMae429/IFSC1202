n=int(input("Enter Number of Cards: "))
ctot= (n/2) * (1 + n)
csum=0
for x in range(1,n):
  csum+=int(input("Enter Card: "))
print("Missing Card:",int(ctot-csum))