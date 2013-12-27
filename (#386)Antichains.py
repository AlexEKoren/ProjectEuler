def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve
b=20
primes=Primes(b)
print "done"
def factor():
    sieve=[0]*(b+1)
    sieve2=[0]*(b+1)
    sieve[:2]=[0,1]
    for x in xrange(2, len(sieve)):
        if primes[x]:
            for y in xrange(x,len(sieve),x):
                sieve[y]+=1
    for x in xrange(2,int(len(sieve)**.5)+1):
        if primes[x]:
            for y in xrange(x**2,len(sieve),x**2):
                sieve2[y]+=1
    return sieve, sieve2

def factorize():
    sieve=[[]]*(b+1)
    for x in xrange(2,len(sieve)):
        if primes[x]:
            sieve[x]=[x]
    print sieve
    for x in xrange(2,len(sieve)):
        print x
        if primes[x]:
            count=2
            for y in xrange(x*2,len(sieve),x):
                #sieve[y]=sieve[y]+[x]
                add=[x,count]
                print y, count
                if not primes[count]
                    sieve[y]=sieve[y]+sieve[count]
                count+=1
    return sieve

print factorize()
tris=[1,2,3]
def tri(x):
    if x>len(tris):
        tris.append((x-1)*x/2)
        return (x-1)*x/2
    return tris[x-1]

def main():
    total=0
    f,f2=factor()
    print "done"
    for x in xrange(1,len(f)):
        y=f[x]
        z=f2[x]
        #print y
        '''if z>3:
            print x, tri(y), z'''
        if y==1:
            total+=1
            #print x, y, z, 1, total
        elif y==2 and z==2:
            total+=3
            #print x, y, z, 3, total
        elif y==2 and z==1:
            total+=2
            #print x, y, z, 2, total
        else:
            total+=tri(y)
            #print x, y, z, tri(y)+z, total
            total+=z
        if x==10000:
            print x, y, tri(y),z, total
        if x==2*2*3*5*7*11:
            print x, y, tri(y), z
        #print x, y, z, tri(y)+z, total
    print total, x
    
main()
def factor2(x):
    a=set([1])
    if x%2==0:
        for y in range(2,int(x**.5+1)):
            if x%y==0:
                a.add(y)
                a.add(x/y)
        a=list(a)
        a.sort()
        return a
    else:
        for y in range(3,int(x**.5+1),2):
            if x%y==0:
                a.add(y)
                a.add(x/y)
        return a
    return a
    
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

def checkSubs(n):
    a=factor2(n)
    #print a
    for x in reversed(f(a)):
        b=False
        for y in x:
            for z in x:
                if y!=z:
                    if y%z==0:
                        b=True
            if b==True:
                break
        if b==False:
            #print x
            return x
    return 0

def main2(a):
    global primes
    p=Primes(a)
    total=0
    for x in range(len(p)):
        if p[x]:
            primes.append(x)
    for x in range(1,a+1):
        total+=len(checkSubs(x))
        #print "x: ",x, "S(x): ", checkSubs(x), "factors: ",factor(x), "length: ",len(factor(x))
        print "x: ", x, "S(x): ", len(checkSubs(x)), checkSubs(x)
    print total
#main2(100)
#print factor2(44100)
                        
            
