import time
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

        
def totient(n):
    return reduce(mul, ((p-1) * p ** (exp-1) for p, exp in factorize(n)), 1)

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a,b):
    t=time.time()
    primes=Primes(a)
    print time.time()-t
    chainNums=[1]
    chainValues=[1]
    total=0
    c=False
    for x in range(2, a):
        if primes[x]:
            tempChain=[x]
            tempValues=[]
            #print x
            temp=x-1
            count=1
            while temp not in chainNums:
                tempChain.append(temp)
                temp=totient(temp)
                count+=1
            #print temp
            check=chainValues[chainNums.index(temp)]+count
            value=check
            '''for y in tempChain:
                chainNums.append(y)
                chainValues.append(value)
                value-=1'''
            chainNums.append(x-1)
            chainValues.append(value-1)
            if check==b:
                c=True
                total+=x
            if c==True:
                print x, check
    print total, time.time()-t
    '''for x in range(len(chainNums)):
        print chainNums[x], chainValues[x]'''

main(500000, 20)




            
    
