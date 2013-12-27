import time
def Primes(x):
    primes=[2]
    for y in range(3, x, 2):
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(y)
    return primes
def main2(x):
    primes=Primes(x)
    y=2
    total=0
    while y<len(primes)-1:
        p1=primes[y]
        p2=primes[y+1]
        temp=p2
        while p2%10**len(str(p1))!=p1:
            p2+=temp
        total+=p2
        y+=1
    print total
def main(x):
    t=time.time()
    primes=Primes(x)
    y=2
    total=0
    while y<len(primes)-1:
        p2=primes[y+1]
        p1=primes[y]
        l=len(str(p1))
        a=p2
        q=1
        while (p2*q%10)!=p1%10:
            q+=1
        while a%10**l!=p1:
            a=p2*q
            q=q+10
        #print a, p1, p2
        y+=1
        total+=a
    print total, time.time()-t
#main2(10000)
main(1000000)
