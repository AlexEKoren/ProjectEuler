import time
import fractions
from operator import mul
from collections import defaultdict
from itertools import count
from heapq import merge

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
def findFactors(n):
    x=[1]
    i=2
    while n>1:
        if n%i==0:
            x.append(i)
            while n%i==0:
                n=n/i
        i+=1
    return x

import time
def Primes(y):
    primes=[2]
    i=3
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

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
    
def main(a, n):
    t=time.time()
    count=0
    primes=Primes(n+1)
    #print primes
    print "finished primes"
    for x in range(1,a+1):
        z=x
        for y in primes:
            while z%y==0:
                z/=y
        if z==1:
            count+=1
            print x
    print count, time.time()-t

def main2(a,n):
    t=time.time()
    count=0
    total=a
    array=[]
    sieve=[True]*(a)
    for x in primes():
        if x>n:
            sieve[x::x]=[False]*(a/x)
        if x>a:
            break
    print sieve.count(True), time.time()-t

#main(100,5)      
