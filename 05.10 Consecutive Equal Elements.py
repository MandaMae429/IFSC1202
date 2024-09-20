n=input("Enter a Number (CR to Quit)")
lconseq=0
conseq=1
leader=int(n)
last =-3000
while n!='':
  n=int(n)
  if n==last:
    conseq+=1
  else:
    if conseq>lconseq:
      leader=last
      lconseq= conseq
    conseq=1
  last=n
  n=input("Enter a Number (CR to Quit)")
  if conseq>lconseq:
      leader=last
      lconseq= conseq
print(leader,"repeated",lconseq,"times")