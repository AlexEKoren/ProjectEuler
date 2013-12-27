def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(int(a/x)-1)
    return sieve

def admis(a):
    p=Primes(int(a**.5))
    primes=[x for x in range(len(p)-1) if p[x]]
    admissables=[[],[]]
    m=1
    l=1
    for x in primes:
        m*=x
        if m>a:
            break
        admissables[l].append(m)
        y=x
        while y<=a:
            for z in (admissables[l][:]+admissables[l-1]):
                if z*y<=a:
                    admissables[l].append(z*y)
            y*=x
        l+=1
        admissables.append([])
    final=[]
    for x in admissables:
        for y in set(x):
            final.append(y)
    final=list(set(final))
    final.sort()
    return final

def isPrime(a):
    for x in range(3,int(a**.5)+1,2):
        if a%x==0:
            return False
    return True

def main(a):
    admissables=admis(a)
    final=set([])
    total=0
    for x in admissables:
        y=x+3
        while not isPrime(y):
            y+=2
        final.add(y-x)
    print (sum(final))

#main(10**9)
