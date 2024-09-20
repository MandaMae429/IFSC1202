a=int(input("Enter A: "))
b=int(input("Enter B: "))
if a<b:
  order =1
else:
  order =-1
for x in range(a,b+order,order):
  print(x)