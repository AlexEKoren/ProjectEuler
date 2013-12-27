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

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def f(n):
    count=0
    for x in range(1,n+1):
        for y in range(x, n+1):
            if lcm(x,y)==n:
                #print n, x, y
                count+=1
    return count

def main(a):
    total=0
    for x in range(a):
        #print x,f(x)
        total+=f(x)
    print total

def main2(a):
    total=0
    for x in primes():
        if x>a:
            break
        for y in primes():
            if y<x:
                continue
            elif y>a:
                break
            l=lcm(x,y)
            if l<a:
                total+=int(a/x)/2
    print total-1
main2(10)
