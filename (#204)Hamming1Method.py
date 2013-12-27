import time
import math
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def nex(a,p,limit):
    l=set([])
    for x in a:
        for y in p:
            if y*x<limit:
                l.add(y*x)
            else:
                break
    return l

def main(a,b):
    t=time.time()
    p=Primes(a)
    primes=list(x for x in range(len(p)) if p[x])
    l=set([1])
    n=nex(l,primes,b)
    while len(l.union(n))!=len(l):
        print len(l)
        l=l.union(n)
        n=nex(l,primes,b)
    print len(l), time.time()-t

p=Primes(100)
primes=list(x for x in range(len(p)) if p[x]) 
def main2(l,primes):
    if len(primes)==0:
        return 1
    x=0
    p=primes[0]
    for y in range(int(math.log(l,p))+1):
        x+=main2(l/p**y,primes[1:])
    return x
print main2(10**9,primes)
