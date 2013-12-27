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
            
def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)

def checkD(n,a):
    for x in range(2,a+1):
        if n%x!=0:
            return False
    return True

def findI(a):
    x=factorial(a)
    for y in range(2,a):
        while checkD(x,a):
            x/=y
        x*=y
    return x

def tau(x):
    ti=time.time()
    t=1
    for x in factorize(x):
        t*=(x[1]+1)
    return t

def main(a):
    x=0
    i=findI(29)
    temp=0
    m=0
    while temp<a:
        x+=i
        temp=(tau(x**2)+1)/2
        if temp>m:
            m=temp
            print x,m
    i=findI(25)
    mi=m
    while 1:
        x-=i
        temp=(tau(x**2)+1)/2
        if temp<mi and temp>a:
            print x, mi
            mi=temp
        if x<0:
            break
    print x

main(4000000)
            






            

