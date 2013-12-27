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

def main(a):
    primes=Primes(a)
    for x in primes:
        print x
        num=1
        count=0
        e=0
        while num%x!=0 and e<6:
            while count<10**e+1:
                num*=10
                num+=1
                count+=1
            e+=1
            print e
        if e<6:
            print "yes",x
        
            
main(100)
        
