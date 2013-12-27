import random
import time
n1=5678027
n2=7208785
def findStart(n):
    return n*(n-1)/2 + 1

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in xrange(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def isPrime(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in xrange(1):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def findSurrounding(n,r):
    a=n-(r-1)
    b=n+r
    if a%2==0:
        f=[(a-1),(a+1),b]
    else:
        f=[(b-1),(b+1),a]
    return f

def checkSurrounding(f):
    p=[]
    for y in f:
        if isPrime(y):
            p.append(y)
    return p

def gen():
    while 1:
        yield 4
        yield 2

def main(r):
    t=time.time()
    total=0
    x=findStart(r)
    g=gen()
    while (x-1)%6!=0:
        x+=1
    print x
    i=0
    while x<findStart(r)+r:
        #if (x-1)%6==0 or (x+1)%6==0:
            if isPrime(x):
                f=findSurrounding(x,r)
                p=checkSurrounding(f)
                if len(p)>=2:
                    total+=x
                elif len(p)==1:
                    if p[0]<x:
                        f2=findSurrounding(p[0],r-1)
                        if len(checkSurrounding(f2))>1:
                            total+=x
                    else:
                        f2=findSurrounding(p[0],r+1)
                        if len(checkSurrounding(f2))>1:
                            total+=x
            x+=g.next()
    print total, time.time()-t
    return total
main(100000)
t=time.time()
print main(n1)+main(n2)
print time.time()-t
                    
                    
    



