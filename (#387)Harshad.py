import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

p=[]
primes=[]

def harsh(h):
    nex=set([])
    for x in h:
        for y in range(10):
            total=sumDigits(x)+y
            if (x*10+y)%total==0:
                nex.add(x*10+y)
    return nex

def sumDigits(x):
    t=0
    while x>0:
        t+=x%10
        x/=10
    return t

def strongHarshad(x):
    a=sumDigits(x)
    if x%a==0:
        if p[x/a]:
            return True
    return False

def rightHarshad(x):
    while x>0:
        a=sumDigits(x)
        if x%a==0:
            x/=10
        else:
            break
    if x==0:
        return True
    return False

def isPrime(n):
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        #checks if it has any factors beneath its square root plus 1
        if n%x==0:
            return False
    return True
    #returns true if all else is false.

def main2(a):
    ti=time.time()
    h=set([1,2,4,6,8])
    total=0
    final=set([])
    for x in range(a-2):
        h.update(harsh(h))
    for x in h:
        if isPrime(x/sumDigits(x)):
            final.add(x)
    for x in final:
        #print x
        for y in range(1,10,2):
            t=x*10+y
            if isPrime(t):
                total+=t
                #print len(str(t)), t
    print total, time.time()-ti, len(l)
#main2(14)
main2(14)
