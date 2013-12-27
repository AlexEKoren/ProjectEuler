import time
import math
def rev(s):
    return int(s[::-1])

def makePals(a):
    x=1
    r=rev(str(x))
    #l=[]
    #while x*10+r<a:
    while 1:
        s=str(x)
        yield x*(10**len(s))+r
        n=x*10*(10**len(s))+r
        for y in range(10):
            #l.append(n+(y*10**len(s)))
            yield (n+(y*10**len(s)))
        x+=1
        r=rev(str(x))
    #print l

def makePows(a):
    c=[]
    for x in range(2,a):
        c.append(x**3)
    return c

def isSqr(x):
    return math.sqrt(x).is_integer()
    n=int(x**.5)
    if n*n==x:
        return True
    return False

def main():
    c=makePows(1000000)
    total=0
    co=0
    t=time.time()
    for x in makePals(1):
        #print x
        if x==37088073:
            print "yes"
        count=0
        for cu in c:
            if cu>x:
                break
            sq=x-cu
            if isSqr(sq):
                count+=1
        if count==4:
            print x
            total+=x
            co+=1
        if co==5:
            print total, time.time()-t
            return
    

main()

def isRev(x):
    s=str(x)
    if s==s[::-1]:
        return True
    return False

def main2(a):
    s,c=makePows(100000)
    l=[]
    counts=[]
    #count=0
    total=0
    for sq in s:
        for cu in c:
            if sq+cu>a:
                break
            if isRev(sq+cu):
                if not sq+cu in l:
                    l.append(sq+cu)
                    counts.append(1)
                else:
                    counts[l.index(sq+cu)]+=1
                if counts[l.index(sq+cu)]==4:
                    total+=sq+cu
                    print sq+cu, total
#main2(int(10**(11)))
