import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a, m):
    t=time.time()
    primes=Primes(a)
    x=0
    y=0
    while y<len(primes):
        if primes[y]:
            x+=1
            r=(pow((y-1),x, y**2)+pow((y+1),x, y**2))%(y**2)
            if r>m:
                print x, y, r, time.time()-t
                return
        y+=1
main(10000000,10**12)
            
