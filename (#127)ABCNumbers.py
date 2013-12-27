from fractions import gcd
import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def factorSieve(a):
    p=Primes(a)
    sieve=[[1] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            for y in range(x,a+1,x):
                sieve[y].append(x)
                sieve[y][0]*=x
    return sieve

sieve=factorSieve(120000)
nums=[x for x in range(1,len(sieve))]# if len(sieve[x])<4]

def rad(a,b,c):
    t=1
    for x in sieve[a]:
        t*=x
    for x in sieve[b]:
        t*=x
    for x in sieve[c]:
        t*=x
    return t

def check(c):
    for a in range(1,c/2):
        t=sieve[a][0]*sieve[c][0]
        if t<c/2+1:
            if len([x for x in sieve[a] if x in sieve[c]])==0:
                b=c-a
                if t*sieve[b][0]<c:
                    #print a,b, c
                    return True
    return False

def main2(l):
    t=time.time()
    total=0
    count=0
    for c in nums:
        if c>l:
            break
        #print c
        if sieve[c][0]<c/2+1:
            if check(c):
                total+=c
                count+=1
    print count, total, time.time()-t
    

def checks(a,b):
    #if gcd(a,b)==1:
    if len([x for x in sieve[a] if x in sieve[b]])==0:
        c=a+b
        if rad(a,b,c)<c:
            #print a, b, c
            return c
    return 0

def main(l):
    t=time.time()
    total=0
    i=0
    for a in nums[:nums.index(l)]:
        #if a%1000==0:
            #print a
        for b in nums[i:]:
            if a+b>l:
                break
            total+=checks(a,b)
        i+=1
    print total, time.time()-t

main2(100000)
