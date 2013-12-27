import time
from math import *
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def sieve(a):
    p=Primes(int(sqrt(a))+1)
    sq=[True]*(a+1)
    #print len(sq)
    sq[:2]=[False,False]
    for x in range(len(p)):
        if p[x]:
            s=x**2
            for y in range(s, len(sq), s):
                sq[y]=False
    count=0
    for x in range(len(sq)):
        if sq[x]:
            count+=1
    print log(a,2), ":", count+1

for z in range(20):
    sieve(2**z)
    

def main(ex):
    p=Primes(int((2**ex)**.5))
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    sq=[]
    for x in primes:
        sq.append(x**2)
    count=0
    for n in range(1,2**ex):
        if log(n,2)==int(log(n,2)):
            print log(n,2),count
        b=True
        for x in sq:
            if x>n:
                break
            if n%x==0:
                b=False
                break
        if b==True:
            #print n
            count+=1
    print ex*1.0,count
#main(2)
