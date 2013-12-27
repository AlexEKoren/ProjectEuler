import fractions
import time
def red(n, d):
    array=[]
    gcd=fractions.gcd(n,d)
    if gcd>1:
        array.append(n/gcd)
        array.append(d/gcd)
    else:
        array.append(n)
        array.append(d)
    return array

def Primes(y):
    primes=[2]
    i=3
    while i<y:
        isprime=True
        if i%2!=0:
            for x in range(3, int(i**.5 + 1), 2):
                if i%x==0: 
                    isprime=False
                    break
            if isprime:
                primes.append(i)
        i=i+1
    return primes

def f(k):
    fracNum=1
    fracDenom=k
    while fracNum!=fracDenom and fracDenom!=1:
        #print str(fracNum)+"/"+str(fracDenom)
        temp=fracNum
        tempD=fracDenom
        fracNum=red(temp, tempD)[0]
        #print red(fracNum, fracDenom)[0], red(fracNum, fracDenom)[1]
        fracDenom=red(temp, tempD)[1]
        #print fracDenom
        fracNum+=1
        fracDenom-=1
    if fracNum==fracDenom:
        return 1
    else:
        return fracNum
    
def main(p):
    t=time.time()
    #primes=Primes(p)
    #print primes
    total=0
    for k in range(1,p+1):
        temp=f(k**3)
        print k**3, temp
        total+=f(k**3)
        #print k
    print time.time()-t
    print total#-990100
main(1000)
#print f(3)
        
