import time
import itertools
from math import log
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def remove(p):
    final=[]
    for x in p:
        s=str(x)
        b=True
        if '0' in s:
            b=False
        if b==True:
            for y in s:
                if s.count(y)>1:
                    b=False
                    break
        if b==True:
            final.append(x)
    return final

def genallsubsets(n):
    S = [[i] for i in range(n)]
    for s in S:
        yield s
    N = S
    for k in range(n):
      if N:
           S = N
           N = []
           for e in S:
             for i in range(e[-1]+1,n):
                f = e[:]
                f.append(i)
                yield f
                N.append(f)

def containsAll(a):
    array=[]
    for x in a:
        for y in str(x):
            if not y in array:
                array.append(y)
            else:
                return False
    return True

def main(a):
    p=Primes(10**a-1)                    
    primes=[]
    for x in xrange(len(p)):
        if p[x]:
            primes.append(x)
    print len(primes)
    primes=remove(primes)
    print len(primes)
    count=0
    f=genallsubsets(len(primes))
    while 1:
        x=f.next()
        while len(x)<3:
            x=f.next()
        length=0
        #print x
        #print primes[x[0]],primes[x[1]],primes[x[2]]
        for y in x:
            length+=int(log(primes[y],10))+1
        #print length
        if length==9:
            #print primes[x[0]],primes[x[1]],primes[x[2]]
            temp=[]
            for y in x:
                temp.append(primes[y])
            if containsAll(temp):
                print temp, count+1, x
                count+=1
        else:
            while x[0]==f.next()[0] and x[0]!=24:
                #print x[0]
                x=f.next()
    print count
                
    print count
main(3)
