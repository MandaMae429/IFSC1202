year=(int(input("Enter Year: ")))
if year/400:
    print ("LEAP YEAR: ")
elif year/4 and not year/100:
    print ("LEAP YEAR")
else:
    print ("COMMON YEAR")