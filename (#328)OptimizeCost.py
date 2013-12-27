import time
def bsearch(a, start, b):
    total=start
    l=0
    if a==1:
        low=1
        high=start
    else:
        low=start
        high=a
    while low<high:
        if b!=1 and b==a:
            if b!=1 and l==b-2:
                l=(low+high)/2
            elif (low+high)%2==1:
                l=(low+high)/2+1
            else:
                l=(low+high)/2
        else:
            l=(low+high)/2
        if b!=1:
            if l!=b:
                total+=l
        if b==1 and l!=b and l!=b+1:
            total+=l
        if b==1 and l==b+1:
            total+=1
        if b!=1 and b==a:
            if l==b+1 or l==b-1:
                #print total
                #return
                return total
        if b!=1 and b!=a:
            if l==b-1:
                return total
        if b==1:
            if l==2 or l==1:
                return total
        if l<b:
            low=l+1
        elif l>b: 
            high=l
        else:
            return total
            #print total
            #return

def C(n):
    f=time.time()
    b=2
    if n%2==0:
        if b%2==0:
            b=b+1
    l=b
    mFinal=0
    lFinal=0
    while l<n:
        m=0
        k=bsearch(n,l,n)
        print "k: "+str(k)
        t=bsearch(1,l,l-1)
        print "t: "+str(t)
        #p=bsearch(1,l,1)
        #print "p"+str(p)
        print l
        if l==b:
            mFinal=k
        #m=max(k,p,t)
        #m=max(k,p)
        m=max(k,t)
        if mFinal>m:
            mFinal=m
            lFinal=l
        l+=2
    print mFinal
    #print time.time()-f
    print lFinal
    return mFinal

def main(n):
    t=time.time()
    total=43
    #total=17575
    l=9
    while l<=n:
        print l,C(l)
        total+=C(l)
        l+=1
    t2=time.time()
    print t2-t
    print total
#main(100)
#bsearch(5,,5)
C(100)
        
