rvsh=input("Enter a String: ")
while rvsh.count('h')<2:
  rvsh=input("Enter a String: ")
first=rvsh.find('h')
last=rvsh.rfind('h')
mid=rvsh[first:last+1]
mid=mid[::-1]
print(rvsh[:first]+mid+rvsh[last+1:])