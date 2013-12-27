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
            
def fractions(a):
    count=1
    for x in xrange(a+1,2*a):
        #print x
        num1=1
        denom1=a
        num2=1
        denom2=x
        num1*=denom2
        num2*=denom1
        denom1,denom2=(denom1*denom2),(denom1*denom2)
        num2=num1-num2
        #print num2, denom2
        if denom2%num2==0:
            count+=1
    return count

def main(a):
    for x in range(a):
        print x, fractions(x)
        for y in factorize(x):
            print y

main(20)
