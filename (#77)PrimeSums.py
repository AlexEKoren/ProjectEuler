import time
import itertools
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    array=[0]*(a**2)
    p=Primes(10000)
    primes=[0]*50
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    for x in itertools.combinations(range(len(primes)),50):
        total=primes[x[0]]
        for y in x:
            if total<(a**2) and total>0:
                total+=primes[y]
                #print total
                array[total]+=1
                if array[total]>=a:
                    print total
                    return
            else:
                break
main(5000)
