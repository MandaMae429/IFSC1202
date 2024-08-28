inputdays =(input("Enter Length of Time in Days: "))
days=int(inputdays)
year=days//365
days=days-(year*365)
print("Years: ",year)
week=days//7
days=days-(week*7)
print("Weeks: ",week)
print("Days: ",days)