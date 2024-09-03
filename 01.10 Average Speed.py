kilo=(int(input("Enter Length of Race in Kilometers: ")))
min=(int(input("Enter Minutes: ")))*60
sec=(int(input("Enter Seconds: ")))
kilo1=kilo/1.61
print (float(kilo1/(min+sec))*3600)