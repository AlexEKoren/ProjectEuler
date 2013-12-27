def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    primes=[]
    for x in range(len(sieve)):
        if sieve[x]:
            primes.append(x)
    return primes

def main(a,limit):
    primes=Primes(a)
    x=0
    array=[]
    while x<len(primes):
        p=primes[x]
        print p
        temp=0
        temp+=limit/p
        print temp
        y=0
        while y<x:
            temp-=array[y]/p
            print temp
            y+=1
        array.append(temp)
        x+=1
    print sum(array)

main(5,10)
        
