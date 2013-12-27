import time
from math import *
def findFactors(a):
    f=[]
    for x in range(1,int(a**.5)+1):
        if a%x==0:
            f.append(x)
            f.append(a/x)
    return list(set(f))

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def factors2(n):
    return set(x for tup in ([i, n//i] for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)    

def isSqr(x):
    return sqrt(x).is_integer()

def main(a):
    t=time.time()
    total=0
    for x in range(1,a):
        f=factors2(x)
        temp=sum(y**2 for y in f)
        if isSqr(temp):
            total+=x
            print x, temp
    print total

main(640000)


