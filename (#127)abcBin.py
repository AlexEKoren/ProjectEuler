def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def genFacs(a):
    p = Primes(a)
    z=[]
    for x in range(a+1):
        z.append([])
    for x in range(len(p)):
        if p[x]:
            for y in range(x,a+1,x):
                z[y].append(x)
    return z

def genBin(a):
    z = genFacs(a)
    f = []
    for x in range(a):
        n=0
        for i in range(int(x**.5)+1,1,-1):
            if i in z[x]:
                n<<=1
                n+=1
            else:
                n<<=1
        f.append(n)
    print f

genBin(10)
                
            
    
