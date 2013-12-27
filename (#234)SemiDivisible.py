import time
import math
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def main(a):
    t=time.time()
    p=Primes(a)
    count=0
    total=0
    for x in range(5,a):
        s=math.sqrt(x)
        if int(s)!=s:
            lps=int(s)
            hps=int(s)+1
        else:
            lps=int(s)
            hps=int(s)
        while lps>0:
            if p[lps]:
                break
            lps-=1
        while hps<a:
            if p[hps]:
                break
            hps+=1
        #print x, lps, hps
        if (x%hps==0 and x%lps!=0) or (x%lps==0 and x%hps!=0):
            count+=1
            total+=x
            print x
    print total, count, time.time()-t

main(100)
    
    
