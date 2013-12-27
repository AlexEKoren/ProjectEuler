import time
import fractions
from operator import mul
from collections import defaultdict
from itertools import count

primes_cache, prime_jumps = [], defaultdict(list)

def primes():
    prime = 1
    for i in count():
        if i < len(primes_cache): prime = primes_cache[i]
        else:
            prime += 1
            while prime in prime_jumps:
                for skip in prime_jumps[prime]:
                    prime_jumps[prime + skip] += [skip]
                del prime_jumps[prime]
                prime += 1
            prime_jumps[prime + prime] += [prime]
            primes_cache.append(prime)
        yield prime
        
def factorize(n):
    for prime in primes():
        if prime>n:
            return
        exponent=0
        while n%prime==0:
            exponent+=1
            n/=prime
        if exponent != 0:
            yield prime, exponent

def countI(f):
    return sum(1 for x in f)

def totient(n):
    f=factorize(n)
    '''if countI(f)>2:
        return 1
    else:'''
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in f), 1)

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main2(a):
    f=time.time()
    m=a
    final=0
    p=Primes(a)
    '''primes=[]
    x=0
    while x<len(p):
        if p[x] and x!=2:
            primes.append(x)
        x+=1'''
    x=a/30
    y=x-1
    while x>0:
        while not p[x]:
            x-=1
        y=a/x
        while y>0:
            while not p[y] and y>0:
                y-=1
            if y<=0:
                break
            n=x*y
            if n>a:
                break
            t=x*(y-1)-y+1
            
            if n*1.0/t<m:
                #print n, x, y, t
                temp=list(str(n))
                temp2=list(str(t))
                s1=0
                s2=0
                for z in temp:
                    s1+=int(z)
                for z in temp2:
                    s2+=int(z)
                if s1==s2:
                    temp.sort()
                    temp2.sort()
                    if temp==temp2:
                        print n*1.0/t, n, t, time.time()-f, list(factorize(n))
                        m=n*1.0/t
                        final=n
            y-=1
        x-=1
    print final
print totient(923848226)
#main2(10**7)
            
