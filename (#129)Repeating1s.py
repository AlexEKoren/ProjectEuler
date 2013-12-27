import fractions
import time

def Primes(a,x):
    primes=[]
    for y in range(a+1, x, 2):
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(y)
    return primes

def A(k,x):
    s=1
    count=0
    while s%k!=0:
        s*=10
        s+=1
        count+=1
        '''if count>x:
            return s'''
    return s

def main(a):
    t=time.time()
    #primes=Primes(10**(a),10**(a)+1000)
    primes=Primes(10**a, 10**(a)+1000)
    print primes
    print "primes done"
    count=0
    s=0
    while count<10**a:
        s*=10000000000
        s+=1111111111
        count+=10
    print "s done", time.time()-t#, s
    while 1:
        print count
        for x in primes:
            if s%x==0:
                print x,count
                return x
        s*=10
        s+=1
        count+=1
    '''for x in primes:
        print x
        temp=A(x, 10**(10**a))
        if temp%(10**(10**a))!=temp:
            print time.time()-t
            print x
            return'''
def main2(a, p):
    s=0
    for x in range(a/10):
        s*=10000000000
        s+=1111111111
    if s%p==0:
        print True
    else:
        print False
main2(1000002,1000003)
#main(2)
