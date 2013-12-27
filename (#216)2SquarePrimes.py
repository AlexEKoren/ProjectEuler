import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    p=Primes(a)
    sqrt=2*a**2-1
    count=0
    for n in range(int(sqrt)):
        if p[2*n**2-1]:
            print 2*n**2-1
            count+=1
    print count
main(10000)
