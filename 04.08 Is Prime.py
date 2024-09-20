n=int(input("Enter N:"))
isprime=True
for y in range(2,(n//2)+1):
    if n%y==0:
      isprime=False
      continue
if isprime:
        print("PRIME")
else:
        print("COMPOSITE")