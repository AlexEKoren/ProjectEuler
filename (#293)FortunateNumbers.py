30, 19, 13, 11, 9, 9, 8, 8, 7
def main(limit):
    primes=[2,3,5,7,11,13,17,19,23]
    array=[-1]*limit
    array[0]=-1
    array[1]=-1
    for x in primes:
        i=primes.index(x)
        #print x, i
        for y in xrange(x, len(array), x):
            if array[y]==i-1:
                array[y]+=1
            else:
                array[y]=-1
    count=0
    for x in xrange(len(array)):
        if array[x]!=-1:
            count+=1
            #print x, array[x]
    print count

main(10**9)
                                        
