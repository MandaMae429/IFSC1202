m1=int(input("Enter First Number: "))
m2=int(input("Enter Second Number: "))
count=0
if m2>m1:
  m1,m2=m2,m1
n=input("Enter a Number (CR to Quit)")
while n!='':
  n=int(n)
  if n>m1:
    m2=m1
    m1=n
  n=input("Enter a Number (CR to Quit)")
print("First Maximum:",m1)
print("Second Maximum:",m2)