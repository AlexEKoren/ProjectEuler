import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def mul(n,p):
    b=n%10
    a=n/10
    y=(a+b)/p+1
    r=p*y-(a+b)
    print a+b, y, p, r
    for x in range(1,p):
        if (a+(b*x))%p==0:
            if n%p==0:
                return x
    return 0

def main(a):
    t=time.time()
    primes=Primes(a)
    primes[5]=False
    total=0
    for x in range(3,a):
        if primes[x]:
            #print x, mul(x,x)
            total+=mul(x,x)
    print total,time.time()-t

main(100000)
            
