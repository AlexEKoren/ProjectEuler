import random
import time

def Primes(a):
    t=time.time()
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def upperPrimeSieve(begin,end):
    sieve=[True]*(end-begin+1)
    p=Primes(int(end**.5))
    for x in range(2,int(end**.5)):
        if p[x]:
            for y in range(x-2,end-begin,x):
                sieve[y]=False
    print sieve.count(True)


#main(5000000)
upperPrimeSieve(0,10000)
                
