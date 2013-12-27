import math
import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    t=time.time()
    p=Primes(a+5)
    primes=[]
    m=0
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    total=0
    for x in range(2,len(primes)-1):
        p1=primes[x]
        l=10**(int(math.log(p1,10))+1)
        p2=primes[x+1]
        count=0
        temp=l
        temp2=p2-p1
        mul=10
        b=False
        y=0
        while b==False:
            for y in range(y,mul, mul/10):
                if (p2*y)%mul==p1%mul:
                    if (p2*y)%l==p1:
                        total+=p2*y
                        b=True
                        break
                    break
            mul*=10
        #print p1, p2, temp, temp/p2+1, count
    print total, time.time()-t, m
main(1000000)
