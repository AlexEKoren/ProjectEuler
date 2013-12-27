import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(y):
    t=time.time()
    total=0
    primes=Primes(y**2+27)
    for x in range(10,y):
        #print x
        y=x**2
        if primes[y+1]:
            if primes[y+3]:
                if primes[y+7]:
                    if primes[y+9]:
                        if primes[y+13]:
                            if primes[y+27]:
                                total+=x
                                print x
    print total, time.time()-t
main(10000)
