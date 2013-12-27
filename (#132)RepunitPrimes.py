import time
from math import log
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def R(n):
    return (10**n-1)/9

def main(a,c):
    p=Primes(a)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    l=[]
    print 2**c*5**c
    mod=100
    n=(10**(2**c*5**c)-1)/9
    for x in range(11):
        div=10**(2**x)+1
        if n%div==0:
            n/=div
            print log(div,10)
    print "done", log(n,10)
    for p in primes:
        if n%p==0:
            n/=p
            l.append(p)
            print p, len(l)
        if len(l)==40:
            break
    print l, sum(l[:40])
    
main(1000000,6)
