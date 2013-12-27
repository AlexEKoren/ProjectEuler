import time
import re
import itertools
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def findOcc(x, s):
    return list(m.start() for m in re.finditer(x, s))

def toString(x):
    s=""
    for y in x:
        s+=y
    return s

def main(a):
    p=Primes(a)
    primes=[]
    nums=[]
    for n in range(10):
        nums.append(str(n))
    for x in range(10**5, 10**6):
        if p[x]:
            primes.append(x)
    for x in primes:
        s=str(x)
        l=list(s)
        for n in nums:
            count=0
            if s.count(n)>1:
                occs=findOcc(n,s)
                for m in nums:
                    tempL=l
                    for y in occs:
                        tempL[y]=m
                    tempI=int(toString(tempL))
                    if tempI in primes:
                        count+=1
                        #print tempI
            if count>=6:
                print x, count, n
            if count>=8:
                print x
                return

main(10**6)
            
