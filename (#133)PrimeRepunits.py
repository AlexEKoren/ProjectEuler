def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a,c):
    p=Primes(a)
    primes=[]
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    array=[1]
    for x in range(1,c):
        temp=(10**(10**x)-1)/9
        temp/=array[-1]
        array.append(temp)
    print array[:1]
    for x in primes[:]:
        b=True
        for y in array:
            if y%x==0:
                y/=x
                #print y,x
                b=False
                break
        if b==False:
            primes.remove(x)
    print sum(primes), primes[:5]

main(100000,6)
