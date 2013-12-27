import time
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
def Primes(y):
    primes=[2]
    i=3
    while i<y:
        isprime=True
        for x in range(2, int(i**.5 + 1)):
            if i%x==0: 
                isprime=False
                break
        if isprime:
            primes.append(i)
        i=i+1
    return primes

def main():
    t=time.time()
    primes=Primes(200000)
    print "done"
    total=0
    l=0
    final=0
    f=0
    while l<len(primes):
        m=l
        sub=0
        while m<len(primes):
            sub+=1
            total+=primes[m]
            if total>1000000:
                break
            if isPrime(total) and sub>final:
                final=sub
                f=total
                print sub,f
            m+=1
        m=l+1
        total=0
        sub=0
        l+=1
    print f, time.time()-t
main()
