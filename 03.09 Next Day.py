month=(int(input("Enter Month: ")))
day=(int(input("Enter Day: ")))
if month==2:
    dlimit=28
elif month==4 or month==6 or month==9 or month==11:
    dlimit=30
else:
    dlimit=31
if day>=dlimit:
    day=1
    if month>=12:
        month=1
    else:
        month+=1
else:
    day+=1
print ("Next Day: ",month,"/", day)
 