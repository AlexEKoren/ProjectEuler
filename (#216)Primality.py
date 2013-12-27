def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    p=Primes(a**2)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    count=0
    for x in range(2,a):
        if(2*x**2-1) in primes:
            #print x, 2*x**2-1
            count+=1
    print count

main(10)
