import time
from fractions import *
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
        if prime > n: return
        exponent = 0
        while n % prime == 0:
            exponent, n = exponent + 1, n / prime
        if exponent != 0:
            yield prime, exponent

        
def totient2(n):
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1)

def main2():
    t=time.time()
    n=15499/94744.0
    m=100
    temp=1
    temp2=2
    i=1
    x=2
    while x<1000000000:
        count=totient2(x)
        #print count, x, temp, temp2
        if temp==temp2 and count*1.0/(x-1)<m:
            temp2=x
            i=temp2-temp
        elif count*1.0/(x-1)<m:
            print "yes", x
            temp=x
            temp2=x
            m=count*1.0/(x-1)
        if count*1.0/(x-1)<n:
            print count, x, count*1.0/(x-1), n
            print time.time()-t
            #print x, count*1.0/(x-1)
            break
            #return
        x+=i
main2()
    
