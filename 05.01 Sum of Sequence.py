i=True
sum =0
while i:
  n=input("Enter a Number (CR to Quit)")
  if n!='':
    sum+=int(n)
  else:
    print("Sum:",sum)
    i=False
