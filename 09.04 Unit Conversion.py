#Download 09.04 Conversion.txt and upload it to your development system (See bottom of page).
#Create a python program that performs unit conversions. You code should do the following:
#Prompt for a floating point number (FromValue). Your prompt should display "Enter From Value: "
#Prompt for the unit to convert from (FromUnit). Your prompt should display "Enter From Unit (mm, cm, m, km, in, yd, mi):"
#Prompt for the unit to convert to (ToUnit). Your prompt should display "Enter To Unit (mm, cm, m, km, in, yd, mi):"
#Open the file 09.04 Conversion.txt file and read it into a 2 dimensional list.
#The first row contains the names of the valid ToUnits.
#The first column contains the names of the valid FromUnits.
#Using a FOR loop, seach for a match between the entered FromUnit and the first column. Save the index of the row that you find the match.
#If no match was found for the FromUnit, then print "FromUnit is not valid" and exit the program
#Using a FOR loop, seach for a match between the entered ToUnit and the first row. Save the index of the column that you find the match.
#If no match was found for the ToUnit, then print "ToUnit is not valid" and exit the program
#Using the index, get the multiplier from the 2D list, multiply it by the FromValue, round to 7 digits, and displays the result as shown.