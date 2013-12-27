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

def totient(n):
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1)

def factorial(x):
    return reduce(mul, (x for x in range(1,x+1)), 1)

def sumUp(x):
    return sum(range(1,x+1))

def Primes(a):
    sieve=[True]*(a+1)
    total=0
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2,sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def factorize(n):
    for prime in primes:
        if prime > n: return
        exponent = 0
        while n % prime == 0:
            exponent, n = exponent + 1, n / prime
        if exponent != 0:
            yield prime, exponent

m=1000001
p=Primes(m)
primes=[]
for x in range(m):
    if p[x]:
        primes.append(x)

        
def main(a):
    t=time.time()
    p=Primes(a+1)
    nums=[]
    final=0
    for x in range(a+1):
        if p[x]:
            nums.append([x,x-1])
        else:
            nums.append([x,0])
    for x in nums:
        if x[1]==0:
            total=1
            for y in factorize(x[0]):
                total*=nums[y[0]][1]*y[0]**(y[1]-1)
            x[1]=total
    for x in nums:
        if x[0]==0 or x[0]==1:
            continue
        #print x
        final+=x[1]
    print final, time.time()-t

#main(m-1)

def main2(a):
    t=time.time()
    array=[]
    for x in range(a+1):
        array.append(x)
    for x in xrange(1, a+1):                                                      
        y=2                                                                 
        while x*y<=a:
            array[x*y]-=array[x]                                                          
            y+=1
    print sum(array)-1, time.time()-t

main2(1000000)



