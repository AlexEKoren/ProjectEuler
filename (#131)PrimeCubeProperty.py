import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def root3rd(x): 
    y, y1 = None, 2 
    while y!=y1: 
        y = y1 
        y3 = y**3 
        d = (2*y3+x) 
        y1 = (y*(y3+2*x)+d//2)//d 
    return y 

def isCube(x):
    y=int(x**(1./3))+1
    if y*y*y==x:
        return True
    return False

def main(a):
    p=Primes(a)
    primes=[]
    count=1
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    c=1
    for p in primes:
        #print p
        for n in range(c,c+30):
            #print p, n, n**3+n**2*p
            if isCube(n**9+n**6*p):
                c=n+1
                count+=1
                print p,n
                break
    print count

#print root3rd(62)
main(1000000)

def find(n):
    s=[]
    c=[]
    for x in range(1,n):
        s.append(x**2)
        c.append(x**3)
    return s,c

def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2:
        #2 is the first prime number
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
    '''p=Primes(a)
    primes=[]
    count=0
    for x in range(len(p)):
        if p[x]:
            primes.append(x)'''
    s,c=find(10000)
    for x in c:
        for y in c:
            if y>=x:
                break
            temp=x-y
            temp2=round(y**(2./3))
            temp3=temp/temp2
            if temp3==int(temp3):
                if temp3<a:
                    if isPrime(temp3):
                        print temp/temp2, temp2**.5
                        break
               

