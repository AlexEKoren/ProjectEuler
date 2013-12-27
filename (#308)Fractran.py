import time
import math
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
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

a=1000
#104744
p=Primes(a)
nums=[2**x for x in range(len(p)) if p[x]]
seq=[[17,91],[78,85],[19,51],[23,38],[29,33],[77,29],[95,23],[77,19],[1,17],
     [11,13],[13,11],[15,2],[1,7],[55,1]]

def isMul(x,i):
    x*=seq[i][0]
    return x%seq[i][1]==0

def iterate(x):
    for i in range(len(seq)):
        if isMul(x,i):
            return x*seq[i][0]/seq[i][1]

    print x
    return 0

def main():
    x=2
    count=0
    print nums[-1]
    while x!=nums[-1]:
        #print x
        x=iterate(x)
        count+=1
        if x in nums:
            print x, math.log(x,2), count, [y for y in factorize(count)]

main()
    
