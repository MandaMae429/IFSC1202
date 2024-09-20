n=input("Enter a Number (CR to Quit)")
count=0
m=int(n)
while n!='':
  if int(n)>m:
    m=int(n)
    count=1
  elif int(n)==m:
    count+=1
  n=input("Enter a Number (CR to Quit)")
print("Maximum:",m)
print("Number of occurances:",count)