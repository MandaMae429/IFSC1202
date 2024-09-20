n=input("Enter a Number (CR to Quit)")
count=0
prev=int(n)
while n!='':
  if int(n)>prev:
    count+=1
  prev=int(n)
  n=input("Enter a Number (CR to Quit)")
  if count==0:
    print("Sequence length is 0")
else:
    print("Number of Values Greater than Previous",count)