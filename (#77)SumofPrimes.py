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
    temp=Primes(a)
    primes=[0]
    for x in range(len(temp)):
        if temp[x]:
            primes.append(x)
    nums=[0]*sum(primes)*30
    m=10**10
    for x in itertools.combinations_with_replacement(primes, 10):
        #print x, sum(x)
        s=sum(x)
        if s<m:
            nums[s]+=1
            if nums[s]>=5000:
                m=sum(x)
                print sum(x)
            #return 

p=Primes(200)
primes=[0]

for x in range(len(p)):
    if p[x]:
        primes.append(x)

def p(a, n):
    if a==0:
        return 1
    elif a<0 or n==0:
        return 0
    else:
        return p(a, n-1)+p(a-primes[n], n)

def main2(x):
    y=1
    while p(y, len(primes)-1)<x:
        y+=1
    print y
		

main2(5000)
            
