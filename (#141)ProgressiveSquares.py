import time
import math
import itertools
def Primes(a):
    t=time.time()
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def factorSieve(a):
    t=time.time()
    p=Primes(a)
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            y=x
            while y<a:
                for z in range(y, a+1, y):
                    sieve[z].append(x)
                y*=x
    return sieve

def factorSieve2(a):
    sieve=[set([1]) for x in range(a+1)]
    for x in range(2,a):
        for y in range(x, a+1, x):
            sieve[y].add(x)
            if x**2<y:
                sieve[y].add(x**2)
                if x**3<y:
                    sieve[y].add(x**3)
                    if x**4<y:
                        sieve[y].add(x**4)
                        if x**5<y:
                            sieve[y].add(x**5)
                            if x**6<y:
                                sieve[y].add(x**6)
                    
    return sieve

def isSq(x):
    return math.sqrt(x).is_integer()

def main(a):
    f=factorSieve2(a)
    total=0
    limit=a**2
    print "done"
    l=set([])
    for x in range(1,a):
        fs=f[x]
        #print x, fs
        for y in fs:
            z=x**2/y
            s=[x,y,z]
            r=min(s)
            s.remove(r)
            q=max(x,y,z)
            s.remove(q)
            d=s[0]
            n1=q*d+r
            if n1<limit:
                if isSq(n1):
                    if q*1./d==d*1./r:
                        l.add(n1)
                        print str(x)+": ", q, d, r, n1, sum(l)
    print sum(l)

def main2(a):
    t=time.time()
    l=set([9])
    limit=a**2
    print limit
    for x in range(2,int(math.sqrt(a))+1):
        for num in range(2,int(math.sqrt(a/x))+1):
            for denom in range(1,num):
                if x%(denom**2)!=0:
                    continue
                r=x
                d=x*num/denom
                q=d*num/denom
                n=q*d+r
                if n<limit:
                    if isSq(n):
                        print q, d, r, n, sum(l)
                        l.add(n)
    print sum(l),time.time()-t

main(10**4)
