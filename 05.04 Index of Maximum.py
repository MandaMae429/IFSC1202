i=True
count =0
mx =0
ind=0
while i:
  n=input("Enter a Number (CR to Quit)")
  if n!='':
    if mx<int(n):
      count+=1
      mx=int(n)
      ind=count
    else:
      count+=1
  else:
    if count>0:
      print("Maximum:",mx)
      print("Index:",ind)
    else:
      print("Sequence length is 0")
    break