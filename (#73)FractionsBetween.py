import time
import fractions

def isReduced(a,b):
    return fractions.gcd(a,b)==1

def reduced(a, b):
    x=fractions.gcd(a,b)
    return [a/x,b/x]

def Primes(x):
    primes=[1,2]
    for y in range(3, x, 2):
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(y)
    return primes

def main(z):
    t=time.time()
    #primes=Primes(z)
    fracs=[]
    for d in range(2,z+1):
        for n in range(1,d):
            x=n*1.0/d
            if x>1.0/3 and x<1.0/2:
                if isReduced(n,d)==True:
                    fracs.append(n*1.0/d)
            #print n, d
        #print d
    #fracs=list(set(fracs))
    #print fracs
    print time.time()-t
    print len(fracs)
        
            
main(12000)
