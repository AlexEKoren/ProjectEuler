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
            
def squares(a,x):
    s=[]
    for y in range(a,x+1):
        if y%3==0:
            s.append(y**2)
    return s

def isSC(x):
    if x**.5==int(x**.5) or abs(round(x**(1.0/3))-x**(1.0/3))<.000001:
        return True
    return False

def main(a,b):
    t=time.time()
    s=squares(int(a**.5)+1,int(b**.5))
    md=2
    total=9+16900+97344
    for x in s:
        #print x
        for d in range(int(x**.5*.2),int(x**.5)):
            r=x%d
            if r!=0:#and isSC(r)==True:
                q=int(x/d)
                '''if d>q and q>r:
                    if d*1.0/q==q*1.0/r:
                        total+=x
                        print "1",x, x**.5, d, q, r
                        break
                elif d>r and r>q:
                    if d*1.0/r==r*1.0/q:
                        total+=x
                        print "2",x, x**.5, d, q, r
                        break'''
                #if q>d and d>r:
                if q*1.0/d==d*1.0/r:
                    total+=x
                    print "3",x, x**.5, d, q, r
                    #md=d
                    break
    print time.time()-t
    print total
main(10**1,10**7)
