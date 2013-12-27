import time
import math
facs=[]
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def S(p):
    return sum(facs[p-k] for k in range(1,6))%p

def findFacs(a):
    facs=[1]
    num=1
    for x in range(2,a):
        facs.append(num)
        num*=x
    return facs

def main(a):
    t=time.time()
    p=Primes(a)
    primes=[]
    for x in range(13,len(p)):
        if p[x]:
            primes.append(x)
    print time.time()-t
    final=9
    i=-2
    count=1
    for x in primes:
        num=(x-1)/2
        temp=num
        temp+=((num+i)*num)%x
        print x, ((num+i)*num)%x
        if count%2==0:
            i*=-1
        else:
            i*=-1
            i+=1
        count+=1
        final+=temp
    print final, time.time()-t

def S(x):
    total=0
    total+=x-1
    total+=1
    print x, (x-1)/(((x-2)*(x-1))%x)
    total+=(x-1)/(((x-2)*(x-1))%x)
    print x, (x-1)/(((x-3)*(x-2)*(x-1))%x)
    total+=(x-1)/(((x-3)*(x-2)*(x-1))%x)
    print x, (x-1)/(((x-4)*(x-3)*(x-2)*(x-1))%x)
    total+=(x-1)/(((x-4)*(x-3)*(x-2)*(x-1))%x)
    return total%x

def main2(a):
    t=time.time()
    p=Primes(a)
    primes=[]
    for x in range(5,len(p)):
        if p[x]:
            primes.append(x)
    print time.time()-t
    final=0
    for x in primes:
        final+=S2(x)
    print final
    
def S2(a):
    global facs
    facs=findFacs(a+2)
    #print facs
    total=0
    for x in range(4,5):
        print a-x,": ", facs[a-x]%a, a
        total+=facs[a-x]
    return total%a

def main3(a):
    t=time.time()
    p=Primes(a)
    primes=[]
    for x in xrange(5,len(p)):
        if p[x]:
            primes.append(x)
    print time.time()-t
    final=0
    for x in primes:
        '''temp=0
        num=x-1
        denom=(x-1.)*(x-2)
        temp+=fracMod(num/denom,x)
        denom*=(x-3)
        temp+=math.fmod(num/denom,x)
        denom*=(x-4)
        temp+=math.fmod(num/denom,x)
        print temp
        final+=temp'''
        final+=(x-3)*extendedEuclidean(8%x,x)%x
    print final, time.time()-t

def extendedEuclidean(n,d):
    y=n
    x=d
    a=0
    b=1
    while y!=0:
        z=x%y
        c=a-x/y*b
        x=y
        y=z
        a=b
        b=c
    return (a+d)%d

def main4(a):
    t=time.time()
    p=Primes(a)
    primes=[]
    for x in xrange(5,len(p)):
        if p[x]:
            primes.append(x)
    print time.time()-t
    final=0
    for x in primes:
        final+=S4(x)
    print final

def S4(x):
    y=3*x%8
    return (y*x-3)//8
#main(50)
#main2(50)
main4(10**8)

    
