import time
from itertools import izip
import operator as op

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
            
def fact(n, r):
    temp1=1
    temp2=1
    for i in range(2, r+1):
        temp1*=i
        temp2*=(n-i+2)
    temp2*=(n-i+1)
    return temp2/temp1

def main(n, r, a):
    tempn=n
    tempr=r
    array=[]
    for z in range(0,a):
        t=time.time()
        tempn=n*10**z
        tempr=r*10**z
        print tempn, tempr
        f=fact3(tempn, tempr)
        total=0
        #print f
        #print list(factorize(f))
        for x in factorize(f):
            for y in range(x[1]):
                total+=x[0]
        #print time.time()-t
        print total
        array.append(total)
    x=0
    while x<len(array)-1:
        print x+1, x+2, array[x+1]*1.0/array[x]
        x+=1

def fact2(n, r):
    return reduce(lambda x, y: x * y[0] / y[1], izip(xrange(n - r + 1, n+1), xrange(1, r+1)), 1)

def fact3(n, r):
    r = min(r, n-r)
    if r == 0: return n
    num = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return num//denom
        
main(20000,15000,1)
