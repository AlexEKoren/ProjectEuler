import itertools
import time
def isPrime(a):
    if a<2:
        return False
    if a==2:
        return True
    if a%2==0:
        return False
    for x in range(3,int(a**.5)+1,2):
        if a%x==0:
            return False
    return True

def partitions(s,p,perm):
    c = 0
    for x in range(s,len(perm)):
        n = 0
        for y in perm[s:x+1]:
            n*=10
            n+=y
        if n < p:
            continue
        if not isPrime(n):
            continue
        if x==len(perm)-1:
            #print perm, n, past
            return c + 1
        c+=partitions(x+1,n,perm)
    return c
            

def main():
    t=time.time()
    #print len(range(1,10))
    count=0
    for x in itertools.permutations(range(1,10),9):
        p = partitions(0,0,x)
        if p > 0:
            #print p, x, count
            count+=p
            #print count
    print count, time.time()-t

main()
