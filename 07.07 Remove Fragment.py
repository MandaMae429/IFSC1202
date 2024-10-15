rmvh=input("Enter a String: ")
while rmvh.count('h')<2:
  rmvh=input("Enter a String: ")
first=rmvh.find('h')
last=rmvh.rfind('h')
print(rmvh[:first]+rmvh[last+1:])