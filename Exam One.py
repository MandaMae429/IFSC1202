#human even, NPC odd
#sum of 2 numbers even point for human, odd NPC if int(n)%2==0:
#title
print ("Winners and Losers - Human is Even, Computer is Odd")
comp=0
human=0
for x in range(1,6):
    print ("Round:{}".format(x))
#play 5 rounds
#display round number
#prompt for human number choice
    n=int(input("Enter Your Guess: "))
    from random import randint
    m = randint(1,5)
    print ("Human Guess: {} - Computer Guess: {}".format(n,m))
#print sum is odd or even
    sum=m+n
    if sum %2==0:
        print ("Sum is Even")
        human+=1
    else:
        print ("Sum is Odd")
        comp+=1
    print ("Human Score: {} - Computer Score: {}".format(human,comp))
if human>comp:
        print ("Human Wins")
else:
        print("Computer Wins")

#print Score:
#repeat 5 total times
#finish with human wins computer wins per highest score
