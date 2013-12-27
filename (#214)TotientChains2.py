from itertools import chain, combinations
import time

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(0, len(ss)+1)))

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def composites(factors, N) :
    """
    Generates all number-totient pairs below N, unordered, from the prime factors.
    """
    ps = sorted(set(factors))
    omega = len(ps)

    def rec_gen(n = 0) :
        if n == omega :
            yield (1,1)
        else :
            pows = [(1,1)]
            val = ps[n]
            while val <= N :
                pows += [(val, val - pows[-1][0])]
                val *= ps[n]
            for q, phi_q in rec_gen(n + 1) :
                for p, phi_p in pows :
                    if p * q > N :
                        break
                    else :
                        yield p * q, phi_p * phi_q

    for p in rec_gen() :
        yield p
        
def main(a):
    for x in composites([2,3],20):
        print x
    p=Primes(a)
    primes=[]
    total=0
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    array=[]
    for x in range(1,a):
        array.append([x,x])
    for x in primes:
        #print x
        i=x
        c=x
        m=(x-1)*1.0/(x)
        while c<len(array)+1:
            #print x, c
            array[c-1][1]*=m
            c+=i
    #print "done", array
    for x in array:
        count=1
        temp=x[0]
        while temp!=1:
            temp=array[int(temp)-1][1]
            count+=1
            #print temp, x
        if count==25 and x[0] in primes:
            total+=x[0]
            #print x
    print total
main(40000000)

        
