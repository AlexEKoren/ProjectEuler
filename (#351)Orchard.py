import time
def orchard(a):
    t=time.time()
    sieve=[x-1 for x in range(a+1)]
    sieve[0]=0
    sieve[1]=0
    for x in xrange(2,len(sieve)):
        temp=sieve[x]
        #sieve[x*2::x]=[y-temp for y in sieve[x*2::x]]
        for y in xrange(2*x, len(sieve), x):
            sieve[y]-=temp
    #print sieve
    #print time.time()-t
    #print ((a-1)*(a)/2-sum(sieve))*6+(a-1)*6, time.time()-t#, sieve, (a-1)*a/2
    return ((a-1)*(a)/2-sum(sieve))*6+(a-1)*6

for x in range(2,20):
    print "x:",x," orchard:",orchard(x)

print orchard(10**5)
