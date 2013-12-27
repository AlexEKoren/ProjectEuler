import math
def Primes(a):
    t=time.time()
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def tosci(x):
    return str(x/(10.**(int(math.log(x,10)))))[:3]#+"e"+str(int(math.log(x,10)))

def fib(limit):
    p=Primes(limit)
    primes=[]
    for x in p:
        if x:
            primes.append(x)
    count=2
    counter=2
    a=1
    b=1
    while True:
        a,b=b,a+b
        counter+=1
        br=True
        for i in primes:
            if i**2>counter:
                break
            if b%i**2==0:
                br=False
                #print "broken",b, i, counter
                break
            i+=1
        if br==True:
            count+=1

        if count==limit:
            print b%(10**16), tosci(b)
            break
math.log(10**20938432,10)
fib(10000)
