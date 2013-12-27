import itertools
import time
def main(a):
    t=time.time()
    #Create all the combinations.
    #For a 4 turn game, there are 5 sets
    #4 of them, each number is the turn where the game is lost
    #The final one which contains a "1" means that none of the turns are lost
    i=list(itertools.combinations(list(range(2,a+2))+[1]*(a-(int(a/2)+1)),a-(int(a/2)+1)))
    final=i
    #Sorts the array to skip over any duplicates by adding to the index
    final.sort()
    total=0
    b=0
    while b<len(final):
        x=final[b]
        print x
        temp=1
        #Multiplies the inverse of the number if its not in the set
        #Other wise it multiplies (x-1)/x
        for y in range(2,a+2):
            if y in x:
                temp*=(y-1)*1./y
            else:
                temp*=1./y
        total+=temp
        #Skips over duplicates by incrementing
        while b<len(final)-1 and final[b+1]==x:
            b+=1
        b+=1
    print 1./total, time.time()-t
        

main(15)
