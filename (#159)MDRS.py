import time
def drs(x):
    if x%9!=0:
        return x%9
    return 9

def factorSieve(a):
    sieve=[[drs(x)] for x in range(0,a+1)]
    sieve[0]=[0]
    for x in range(2,len(sieve)):
        for y in range(2*x,len(sieve),x):
            sieve[y].append([x,y/x])
    #print sieve
    return sieve

def main(a):
    t=time.time()
    factors=factorSieve(a-1)
    nums=list([0]*(a))
    for x in range(len(factors)):
        f=factors[x]
        if len(f)==1:
            nums[x]=f[0]
        else:
            m=f[0]
            for y in f[1:]:
                if nums[y[0]]+nums[y[1]]>m:
                    m=nums[y[0]]+nums[y[1]]
            nums[x]=m
    print sum(nums)-1, time.time()-t
main(1000000)
