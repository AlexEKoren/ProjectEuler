from fractions import *
from operator import mul
from collections import defaultdict
from itertools import count
import time

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
    return ((((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1))

def totient3(n):
    total=0
    for x in range(1,n):
        if gcd(x, n)==1:
            print x
            total+=x
    return total

def main(x):
    t=time.time()
    m=0
    a=[]
    for z in range(2,10,2):
        array=[x-z]
        for y in reversed(range(1,x,2)):
            b=True
            for z in array:
                if not gcd(z,y)==1:
                    b=False
            if b==True:# and y%17!=0:
                #print y
                array.append(y)
        if sum(array)>m:
            m=sum(array)
            a=array
    print m,a
    print time.time()-t

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

def main2(n):
    primes=Primes(n)
    array=[]
    for x in primes:
        temp=x
        count=1
        while x+temp<n:
            temp+=x
            count+=1
        print temp, count
        if temp not in array and (count not in primes or count==x):
            array.append(temp)
    print sum(array),array

main(200)
                
