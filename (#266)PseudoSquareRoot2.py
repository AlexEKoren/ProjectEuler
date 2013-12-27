import itertools
import random
import math
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main():    
    p=Primes(190)
    primes=[]
    f=0
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    r=1
    for x in primes:
        #print x
        r*=x
    print long(r)
    num=long(math.sqrt(r))
    m=0
    factors=[]
    random.shuffle(primes)
    count=0
    for x in itertools.product(reversed(primes), repeat=len(primes)-20):
        temp=1
        y=0
        #print x
        while temp<num and y<len(x):
            if temp>m:
                m=temp
                print m%10**16
                print count
            temp*=x[y]
            #print temp
            y+=1
        count+=1
    print m%(10**16)
    
main()
