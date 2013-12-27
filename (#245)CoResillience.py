import time
from fractions import *
from operator import mul
from collections import defaultdict
from itertools import count

primes_cache, prime_jumps = [], defaultdict(list)

def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2:
        #2 is the first prime number
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        #checks if it has any factors beneath its square root plus 1
        if n%x==0:
            return False
    return True
    #returns true if all else is false.

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

        
def totient(n):
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1)

def main(a):
    count=0
    for x in xrange(3,a):
        if not isPrime(x):
            t=totient(x)
            #print x-t,"/",x-1
            if (x-1)%(x-t)==0:
                print "x=",x, "coresillience=",x-t, "/", x-1, "reduced=", "1 /",(x-1)/(x-t), "totient(x)=",t
                count+=1
    print count, a

main(100000)
        
