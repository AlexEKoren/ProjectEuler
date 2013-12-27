from math import sqrt, floor
import time
def factor(x):
    n=1
    a=[]
    for n in range(1, int(x**.5)+1):
        if x%n==0:
            a.append(n)
            a.append(x/n)
    return a

def isSqr(x):
    return sqrt(x).is_integer()

def floorStart(n):
    n=long(n)
    return long((n**2-n%2)/2)

def P(f,r):
    r=long(r)
    f=long(f)
    if r==1:
        return long(floorStart(f))
    if f==1:
        return long(r*(r+1)/2)
    if f%2==0:
        return long(floorStart(f)+(long(floor(r/2))*f*2)+(long(floor((r-1)/2))*(long(floor((r-1)/2))+1))+long((long(floor(r/2)))**2))
    else:
        return long(floorStart(f)+(long((round(r/2.)-1))*f*2)+(long(floor((r-3)/2)))*(long(floor((r-3)/2))+1)+long((long(floor(r/2)))**2))

def main():
    t=time.time()
    a=factor(71328803586048)
    print time.time()-t
    t=time.time()
    x=0
    total=0
    while x<len(a):
        f=a[x]
        r=a[x+1]
        #print f, r
        total+=P(f,r)
        total+=P(r,f)
        x+=2
    print len(str(total))
    print total%(10**8), time.time()-t

main()
