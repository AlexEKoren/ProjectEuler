#finds the smallest number divisible by all numbers below 21

def main():
    i=1000000
    #starting at 20
    while not(i%20==0 and i%19==0 and i%18==0 and i%17==0 and i%16==0 and i%15==0 and i%14==0 and i%13==0 and i%12==0):
        #if it is divisible by any of the above
        while not(i%11==0 and i%7==0):
            #if it is divisible by any of the above
            i=i+2
            #keep adding
    print i

main()
        
