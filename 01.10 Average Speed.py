kilo=(int(input("Enter Length of Race in Kilometers: ")))
min=(int(input("Enter Minutes: ")))*3600
sec=(int(input("Enter Seconds: ")))
kilo1=kilo/1.61
print (int(kilo1/(min+sec)))