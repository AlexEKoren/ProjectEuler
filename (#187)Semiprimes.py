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

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    t=time.time()
    p=Primes(a)
    primes=[]
    '''for x in range(a):
        if p[x]:
            primes.append(x)'''
    primesCount=p.count(True)
    print "primes done", time.time()-t
    total=0
    for x in range(a):
        if p[x]:
            '''count=0
            for y in xrange(x,a/x+1):
                if p[y]:
                    count+=1'''
            #print x
            #temp=p[0:x].count(True)+p[a/x+1:].count(True)
            #total+=primesCount-temp
            total+=p[x:a/x+1].count(True)
    print total
    '''total=0
    for x in primes:
        #print x
        temp=a/x
        if x**2>a:
            break
        while temp not in primes:
            temp-=1
        #print x, total
        total+=primes.index(temp)-primes.index(x)
    print total, time.time()-t'''


def main2(a):
    t=time.time()
    p=Primes(a)
    print "primes done", time.time()-t
    total=0
    primes=[]
    for x in xrange(len(p)):
        if p[x]:
            primes.append(x)
    for x in primes:
        temp=x**2
        for y in primes:
            if x*y<=a:
                if x*y>=temp:
                    #print x, y
                    total+=1
            else:
                break
    print total, time.time()-t
#main(10**5)
main2(10**8)
            
