import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    t=time.time()
    array=[]
    p = Primes(int(a**.5))
    for x in range(len(p)):
        if p[x]:
            array.append(x**2)
    total = a
    print len(array)
    for n in array:
        l = a/n
        count = a/n#+1
        for z in array:
            if z >= min(l,n):
                #count-=1
                break
            count -= count/z
        total-=count
    print total, time.time()-t

def dummy(a):
    p=Primes(int(a**.5)+1)
    primes = []
    for x in range(len(p)):
        if p[x]:
            primes.append(x**2)
    array = [True] * (a+1)
    for x in primes:
        for y in range(x,a+1,x):
            array[y]=False
    print array.count(True)-1, array

main(100)
#dummy(30)
        
