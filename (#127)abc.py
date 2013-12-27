from fractions import gcd
import math, time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve
def factorSieve(a):
    p=Primes(a)
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            y=x
            for z in range(y,a+1,y):
                sieve[z].append(x)
    return sieve

def independent(a,b):
    return any(el in b for el in a)

def main(limit):
    t=time.time()
    f=factorSieve(limit)
    for c in range(limit):
        fc=f[c]
        i=1
        if c%2==0:
            i=2
        for b in range(int(c/2)+1,c,i):
            fb=f[b]
            if independent(fc,fb):
                a=c-b
                fa=f[a]
    print time.time()-t
                
main(10000)
