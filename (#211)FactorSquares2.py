import math
import time

def isSq(x):
    return math.sqrt(x).is_integer()
def factorSieve(a):
    sieve=[1+x**2 for x in range(a+1)]
    sqrt=int(a**.5)+1
    for x in xrange(2,sqrt):
        s=x**2
        for y in xrange(x*(x+1), a, x):
            sieve[y]+=s
            sieve[y]+=(y/x)**2
    return sieve

def factorSieve2(a):
    t=time.time()
    sieve=[0 for x in range(a+1)]
    for x in xrange(1,a):
        s=x**2
        for y in range(x, a+1, x):
            sieve[y]+=s
    print sum(x for x in range(len(sieve)) if isSq(sieve[x])), time.time()-t



def main(a):
    t=time.time()
    l=factorSieve2(a)
    print l
    print "done", time.time()-t
    total=1
    for x in range(len(l)):
        if isSq(l[x]):
            #print math.sqrt(max(x))
            #print x, l[x]
            total+=x
    print total, time.time()-t

factorSieve2(1000000)
