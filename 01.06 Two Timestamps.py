print("First Timestamp")
hours=(int(input("Enter Hours: ")))
min=(int(input("Enter Minutes: ")))
sec=(int(input("Enter Seconds: ")))
print("Second Timestamp")
hours2=(int(input("Enter Hours: ")))*3600
min2=(int(input("Enter Minutes: ")))*60
sec2=(int(input("Enter Seconds: ")))
hours=hours*3600
min=min*60
tsone = hours+min+sec
tstwo=hours2+min2+sec2
print (tstwo-tsone) 