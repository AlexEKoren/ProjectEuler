import time
from fractions import *
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

primes=[]
def rad(a):
    total=1
    for x in primes:
        if x>a:
            break
        if a%x==0:
            #print x
            total*=x
            a/=x
            while a%x==0:
                a/=x
    if a!=1:
        print a
    return total

def main(l):
    global primes
    p=Primes(l)
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    total=0
    Cs=[27,121]
    Bs=[]
    used=[]
    for c in range(1,l):
        Cs.append(c-1)
        for b in Cs:
            a=c-b
            if gcd(c,b)==1 and gcd(b,a)==1:
                if rad(a*b*c)<c:
                    total+=c
                    Cs.append(c)
                    Bs.append(b)
                    Cs=list(set(Cs))
                    print a, b, c
                    for d in range(int(c/2)+1,c):
                        if d not in Cs and d not in Bs:
                            e=c-d
                            if e not in Bs:
                                if e<d:
                                    if gcd(d,c)==1 and gcd(d,e)==1:
                                        if rad(c*d*e)<c:
                                            Bs.append(d)
                                            total+=c
                                            print "2",e, d, c
        Cs.remove(c-1)
    print total

def main2(l):
    t=time.time()
    count=0
    global primes
    p=Primes(l)
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    total=0
    for c in range(1,l):
        for b in range(c/2+1,c):
            a=c-b
            if gcd(c,b)==1 and gcd(b,a)==1:
                if rad(a*b)<c:
                    if rad(a*b*c)<c:
                        total+=c
                        count+=1
                        print a, rad(a), b, rad(b), c, rad(c)
    print total, count, time.time()-t
main2(3000)



