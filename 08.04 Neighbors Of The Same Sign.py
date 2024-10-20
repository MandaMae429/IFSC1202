#Prompt for a string containing integers separated by spaces.
myinput=input("Enter Values Separated by Spaces: ")
#Load the values into a list.
mylist=myinput.split()
#Find and print the first adjacent elements which have the same sign.
negpair=False
pospair=False
for x in range(1,len(mylist)):

    mynumx=int(mylist[x])
    mynumy=int(mylist[x-1])
    if (mynumx*mynumy)>=0:
        
        if mynumy>=0:
            if pospair:
                continue
            else:
                print (mynumy, mynumx)
                pospair=True
        else:
            if negpair:
                continue
            else:
                print (mynumy, mynumx)
                negpair=True
            
    #print (mynum*2)

#If there is no such pair, leave the output blank.