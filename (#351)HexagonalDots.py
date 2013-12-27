import time
def factor(n):
        factors=[]
        for x in range(2,int(n**.5)+1):
                if n%x==0:
                        factors.append(x)
                        if n/x!=x:
                                factors.append(n/x)
        return factors

def onARow(x):
        p=factor(x)
        l=x-1
        for y in factor(x):
                if y==2:
                        l-=1
                else:
                        l-=onARow(y)
        return l

def main(n):
    total=0
    temp=n
    additive=-1
    for x in range(1,temp/2+1):
        if x==1:
            total+=6*(temp-1)
        elif x==2:
            total+=3*(temp-2-temp%2)
        elif x==3:
            total+=12*((temp-x)/x)
        elif x==4:
            total+=12*((temp-x)/x)
        else:
            width=x-1
            facs=factor(x)
            tempFacs=[]
            for f in facs:
                if f>2:
                    tempFacs.append(f)
            for f in tempFacs:
                facs.append(f)
            #print facs
            width-=len(facs)-2
            total+=6*width*((temp-x)/x)
        print x, total
    print total

def main2(n):
    total=6*(n-1)
    temp=n-n%2
    triangle=6*((temp-2)*(temp-3)/2-2)
    total+=triangle
    print total
    
def main3(n):
    total=0
    for x in range(1,n/2+1):
        if x==1:
            total+=6*int((n-1)/x)
        elif x==2:
            total+=3*(n-2-n%2)
        elif x==3:
            total+=12*((n-x)/x)
        else:
            total+=12*int(n/x-1)
        print x, total
    print total

def main4(a):
        f=time.time()
        for n in range(a,a+1):
            tri=[]
            total=6*(n-1)
            #print total
            for x in range(2,n+1):
                tri.append(x-1)
            #print len(tri),tri
            for x in range(n/2-1):
                add=x+2
                t=x+add
                while t<n-1:
                    #print t, add
                    if add==2:
                        tri[t]-=1
                        #total+=6
                    if add>2:
                        tri[t]-=tri[x]
                        #total+=12
                    #print add, total
                    t+=add
            #tri[-1]-=2
            num=1
            x=0
            while x<len(tri):
                total+=6*(num-tri[x])
                #print num,tri[x]
                num+=1
                x+=1
            #print time.time()-f
            print n,total
            #print tri
def main5(n):
    f=time.time()
    total=6*(n-1)
    tri=(n-1)*(n-2)/2
    tri2=tri
    for x in range(2,n/2+1):
        sub=x-1
        for y in range(2,x/2+1):
            if x%y==0:
                #print y, x
                if x==2:
                    sub-=1
                if x>2:
                    sub-=2
        print sub, x
        tri-=sub
    total+=6*(tri2-tri)
    print total

def main6(n):
        f=time.time()
        total=6*(n-1)
        tri=total
        for x in range(2,n/2+1):
                l=onARow(x)
                t=(n-x)/x*l
                tri+=6*((n-x)/x*l)
                #print tri, x, factor(x), t
        print time.time()-f
        print tri

def main7(n):
        f=time.time()
        total=6*(n-1)
        tri=total
        tri+=6*(n-2)/2
        print tri
        for x in range(3, n/2+1):
                #if (n-x)/x==int((n-x)*1.0/x):
                print (n-x)/x*2, x
                tri+=6*(n-x)/x*2
                #else:
                        #tri+=6*((n-x)/x+1)*2
                print x, tri
        print tri

#print factor(5)
#main(10)
#main2(100000)
#main3(10)
main4()
#main5(10)
#main6(10000)
#main7(10)
