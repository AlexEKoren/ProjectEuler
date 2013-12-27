import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(n,r):
    d=n-r
    p=Primes(n)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    top=[]
    for x in range(r+1, n+1):
        if p[x]:
            top.append(x)
            continue
        for y in primes:
            while x%y==0:
                top.append(y)
                x/=y
            if x==1:
                break
    for x in range(2,d+1):
        if p[x]:
            #print x
            top.remove(x)
            continue
        for y in primes:
            while x%y==0:
                top.remove(y)
                x/=y
            if x==1:
                break
    print sum(top)

main(200000,150000)
