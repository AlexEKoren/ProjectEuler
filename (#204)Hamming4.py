import time
import math
import itertools
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a,l):
    p=Primes(a)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    n=1
    m=1
    for x in primes:
        n*=(x-1)
        m*=x
    mul=l*1.0/m
    print n*mul

def main2(z):
    p=Primes(z)
    primes=[]
    for x in range(18,len(p)):
        if p[x]:
            primes.append(x)
    perms=itertools.product(range(8), repeat=18)
    count=0
    for a in range(int(math.log(z,2))):
        print a
        for b in range(int(math.log(z,3))):
            print b
            for c in range(int(math.log(z,5))):
                for d in range(int(math.log(z,7))):
                    for e in range(int(math.log(z,11))):
                        for f in range(int(math.log(z,13))):
                            print f
                            for g in range(int(math.log(z,17))):
                                for h in perms:
                                    print h
                                    if sum(h)>7:
                                        continue
                                    n=2**a*3**b*5**c*7**d*11**e*13**f*17**g
                                    for x in range(len(h)):
                                        n*=primes[x]**h[x]
                                    if n<z:
                                        count+=1
    print count
                                        
main2(100)
