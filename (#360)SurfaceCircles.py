import time
from math import *

def isSquare(x):
    n=sqrt(x)
    if n==int(n):
        return True
    return False
    
def factor(y):
    f=[0,y]
    for x in range(1,int(y**.5)+1):
        if y%x==0:
            f.append(x)
    #print f
    return f

def quad(a,b,c):
    """solves quadratic equations of the form
        aX^2+bX+c, inputs a,b,c,
        works for all roots(real or complex)"""
    root=b**2-4*a*c
    if root <0:
        root=abs(complex(root))
        j=complex(0,1)
        x1=(-b+j+sqrt(root))/2*a
        x2=(-b-j+sqrt(root))/2*a
        return -1,-1
    else:
        x1=(-b+sqrt(root))/2*a
        x2=(-b-sqrt(root))/2*a
        return x1,x2

def main(r):
    t=time.time()
    total2=2*r
    count1=0
    count2=0
    count3=0
    q=r**2
    sq=[]
    for x in range(int(r)+1):
        sq.append(x**2)
    for x in range(int(r)+1):
        x2=x**2
        l=r**2-x**2+1
        y=0
        while y<r:
            g=x2+sq[y]
            if g>q:
                break
            if isSquare(q-g):
                    #print x, y, sqrt(q-g)
                    if (x==0 and y==0) or (x==0 and g==q) or (y==0 and g==q):
                        total2+=2*(abs(x)+abs(y)+abs(sqrt(q-g)))
                        #print x, y, sqrt(q-g)
                        count1+=2
                    elif x==0 or y==0 or g==q:
                        total2+=4*(abs(x)+abs(y)+abs(sqrt(q-g)))
                        #print x, y, sqrt(q-g)
                        count2+=4
                    else:
                        total2+=8*(abs(x)+abs(y)+abs(sqrt(q-g)))
                        #print x, y, sqrt(q-g)
                        count3+=8
            y+=1
    print r,total2,count1, count2, count3,time.time()-t

def main2(r):
    t=time.time()
    total=6*r
    q=r**2
    for x in range(1,r):
        x2=x**2
        for y in range(x, r):
            if x2+y**2==q:
                #print x, y
                total+=24*(x+y)
    for x in range(1, 2*r/3):
        x2=x**2
        for y in range(x, r):
            y2=y**2
            l=q-x2-y2
            if l<=0 or l<y2:
                break
            if l==0:
                total+=24*(x+y)
                #print x, y, sqrt(l), "difference=0"
            elif isSquare(l):
                if x==y or l==y2 or l==x2:
                    total+=24*(x+y+sqrt(l))
                else:
                    total+=48*(x+y+sqrt(l))
                #print x, y, sqrt(l)
    print total, time.time()-t
        
#9765625*1024
#main(1000)
main2(10000)
