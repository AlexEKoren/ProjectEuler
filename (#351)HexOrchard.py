import time
import math
def Primes(a):
    t=time.time()
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def orchard(a):
    sieve=[x-1 for x in range(a+1)]
    sieve[0]=0
    for x in range(2,a/2+1):
        for y in range(2*x,a+1,x):
            sieve[y]-=sieve[x]
    return sum(x-1-sieve[x] for  x in range(4,a+1))

def main(a):
    t=time.time()
    x=orchard(a)
    print x*6+(a-1)*6
    print time.time()-t

main(10000)
