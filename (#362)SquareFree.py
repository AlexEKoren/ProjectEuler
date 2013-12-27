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
    count=0
    for prime in primes():
        if prime>n:
            return count
        b=False
        while n%prime==0:
            b=True
            n/=prime
        if b:
            count+=1

def count_iterable(a):
    return sum(1 for x in a)

def factorial(a):
    return reduce(mul, (x for x in range(1,a+1)),1)
                      
def checkSquare(x):
    f=factorize(x)
    temp=factorial(f)
    print temp, x
    return factorial(f)

def main(l):
    t=time.time()
    print sum(checkSquare(x) for x in range(2,l)), time.time()-t

def Sieve(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    numberSieve=[0]*(a+1)
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
            for y in range((x+1)*x, len(numberSieve), x):
                print y
                numberSieve[y]+=1
    return numberSieve

def main2(a):
    print sum(factorial(x) for x in Sieve(a))-2
#main(10000)
main2(100)
