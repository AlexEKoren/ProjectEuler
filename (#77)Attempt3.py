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

def pent(n):
    return n*(3*n-1)/2

def Xs(y):
    count=0
    x=1
    while x<y:
        if count%2==0:
            yield x
        else:
            yield -1*x
            x+=1
        count+=1
ps=[0,0,1,1,1,1,2,1,3,3,5]
p=Primes(100000)
primes=[]
for x in range(len(p)):
    if p[x]:
        primes.append(x)
        
def p(n):
    if n>=len(ps) and n in primes:
        ps.insert(n, 1)
        return 1
    if n<len(ps):
        return ps[n]
    total=0
    count=1
    for x in Xs(n):
        if pent(x)>n:
            break
        sign=(-1)**(int((count-1)/2))
        total+=sign*p(n-pent(x))
        count+=1
    ps.insert(n, total)
    return total

def main():
    x=1
    while p(x)<5000:
        x+=1
        print x, p(x)
    print x

main()
