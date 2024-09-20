n=input("Enter a Number (CR to Quit)")
count=0
while n!='':
  if int(n)%2==0:
    count+=1
  n=input("Enter a Number (CR to Quit)")
print("Number of Even Values:",count)