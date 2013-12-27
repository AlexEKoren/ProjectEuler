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
    primes=[1]
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
    primes=Primes(10000)
    #print primes
    i=33
    k=1
    yes=False
    while 1==1:
        while k<((i-2)/2)**.5:
            l=0
            while primes[l]+2*(k**2)<=i:
                #print l
                if primes[l]+2*(k**2)==i and not isPrime(i):
                    yes=True
                    break
                l+=1
            #print k
            k+=1
        if yes==False and not isPrime(i):
            print i
            break
        k=1
        i+=2
        yes=False
        #print i
        
        
main()
