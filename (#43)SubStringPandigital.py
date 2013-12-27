import itertools
import time
def Primes(y):
    primes=[]
    i=3
    primes.append(2)
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
    primes=Primes(18)
    print primes
    perms=itertools.permutations([0,1,2,3,4,5,6,7,8,9])
    total=0
    for x in perms:
        i=4
        y=0
        true=""
        p=0
        while i<len(str(x))-6:
            temp=int((str(x))[i]+(str(x))[i+3]+(str(x))[i+6])
            divisible=False
            if temp%primes[p]==0:
                i=i+3
                p=p+1
                divisible=True
            if divisible==False:
                break
        if divisible==True:
            m=1
            q=str(x)
            while m<len(q):
                true=true+q[m]
                m=m+3
            #print true
            total=total+int(true)
            #print total
    print time.time()-t
    print total
main()
            
            
