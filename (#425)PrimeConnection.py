import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

p = Primes(10**3)
primes = [x for x in range(10**3) if p[x]]
connected=set([2])
def isConnected1(a,b):
    if len(a)==len(b):
        c=False
        for x in range(len(a)):
            if a[x]!=b[x] and not c:
                c = True
            elif a[x]!=b[x] and c:
                return False
        if c:
            return True
    return False

def isConnected2(a,b):
    if len(a)==len(b)-1:
        if b[1:]==a:
            return True
        if b[:-1]==a:
            return True
    elif len(b)==len(a)-1:
        if a[1:]==b:
            return True
        if a[:-1]==b:
            return True
    return False

def rec(n, used):
    #print n, used, connected
    #global connected
    if max(used) < n:
        connected.add(n)
    used+=[n]
    s=str(n)
    for x in primes:
        if x in used:
            continue
        if isConnected1(s,str(x)) or isConnected2(s,str(x)):
            print n, x
            rec(x,used)
t=time.time()
rec(2,[2])
print len(connected), len(primes)-len(connected)
connected=list(connected)
connected.sort()
for x in primes:
    if not x in connected:
        print x
print sum(int(x) for x in primes if not x in connected)
print time.time()-t

        
        
    
