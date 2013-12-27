import time
def Primes(x):
    primes=[2]
    for y in range(3, x, 2):
        isPrime=True
        for z in range(3, int(y**.5)+1, 2):
            if y%z==0:
                isPrime=False
                break
        if isPrime==True:
            primes.append(y)
    return primes


def sumUp(t):
    s=0
    for x in list(str(t)):
        s+=int(x)
    return s

def main(a):
    f=time.time()
    primes=Primes(a)
    t=1
    for x in primes:
        t*=x
    print t
    #print sumUp(t)
    x=int(t**.5)
    x2=int(t**.5)
    #print x
    #print sumUp(x)
    while x>0:
        if t%x==0:
            print "x:",x%10**16, "a:",a, t/x, t/x-x
            print time.time()-f
            return
        if t%x2==0:
            print "x2:",t/x%10**16, "a:,",a, t/x2, t/x2-x2
            print time.time()-f
            return
        #print x, x2
        x-=1
        x2+=1
main(60)
