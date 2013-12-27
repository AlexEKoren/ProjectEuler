import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(x):
    t=time.time()
    primes=Primes(x)
    print sum(x for x in range(len(primes)) if primes[x])
    

main(10**6)
