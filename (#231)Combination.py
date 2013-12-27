import time
def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*int(a/x-1)
    return sieve


#p=Primes(2*10**3)
p=[]
primes=[]
#print "done"
def factor(a,b):
    f=[]
    for x in range(len(p)):
        if p[x]:
            exp=0
            l=range(b+(x-b%x),a+1,x)
            '''exp+=len(l)
            while l.count(0)<len(l):
                for y in range(len(l)):
                    l[y]/=x
                for y in range(len(l)):
                    if l[y]%x==0 and l[y]!=0:
                        exp+=1
                    else:
                        l[y]=0'''
            for y in range(len(l)):
                while l[y]>=x and l[y]%x==0:
                    exp+=1
                    l[y]/=x
            f.append(exp)
        if p[x]>a:
            break
    return f

def main(a,b):
    #print a-b
    global p
    global primes
    p=Primes(a)
    primes=[x for x in range(len(p)) if p[x]]
    f1=factor(a,b)
    #print "done"
    f2=factor(a-b,0)
    #print "done"
    #f1=factor(10,7)
    #f2=factor(3,0)
    #print f1, f2
    print (f1[:30])
    #print f2[:30]
    for x in range(len(f2)):
        f1[x]-=f2[x]
    #print f1[:30]
    #print f1[:10],primes[:10]
    print (sum(f1[x]*primes[x] for x in range(len(f1))))

main(2*10**7,int(1.5*10**7))
#main(10,3)
            
    
