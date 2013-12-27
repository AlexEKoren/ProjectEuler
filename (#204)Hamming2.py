import time
import fractions
from operator import mul
from collections import defaultdict
from itertools import count
import itertools
from itertools import chain, combinations

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

def totient2(n):
    t=time.time()
    count=0
    for x in range(n):
        if fractions.gcd(x,n)==1:
            count+=1
    print count, time.time()-t

def combinations(iter):
    return ( set(itertools.compress(iter,mask)) for mask in itertools.product(*[[0,1]]*len(iter)) )

def all_subsets(ss):
  return chain(*map(lambda x: itertools.combinations_with_replacement(ss, x), range(0, int(len(ss)**2.1))))

def mult(a):
    return reduce(mul, (x for x in a), 1)

def main(a,b):
    p=Primes(b)
    primes=[]
    array=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    for x in all_subsets(primes):
        temp=mult(x)
        if temp<=a:
            array.append(temp)
    
    print len(set(array))#, array
        





