import math
from decimal import *
getcontext().prec=400
def contFrac(x):
    rootX=Decimal(x)**Decimal('0.5')
    #print rootX
    f=[int(rootX)]
    temp=rootX-int(rootX)
    while f[0]*2!=f[-1]:
        #print f
        temp=Decimal(1)/temp
        f.append(int(temp))
        temp=(temp-int(temp))
        '''if len(f)>1000:
            getcontext().prec=500
            m=contFrac(x)
            getcontext().prec=100
            return m'''
    return f

def contFrac2(x):
    rootX=math.sqrt(x)
    m=0
    d=1
    a=int(rootX)
    trips=[]
    while [m,d,a] not in trips:
        trips.append([m,d,a])
        m=d*a-m
        d=(x-m**2)/d
        a=int((rootX+m)/d)
    #print len(trips)
    return len(trips)

def main(a):
    total=1
    global cont
    x=3
    while x<a+1:
        while (x-1)**.5==int((x-1)**.5):
            x+=1
            total+=1
        while x**.5==int(x**.5) or (x+1)**.5==int((x+1)**.5) or (x+2)**.5==int((x+2)**.5) or (x-2)**.5==int((x-2)**.5) or x%4==0:
            x+=1
            #total+=1
        if x>a:
            break
        f=contFrac2(x)-1
        #l=len(f)-1
        #print x, l
        #print x, f, l
        if f%2!=0:
            print x
            total+=1
        x+=1
    print total

#print searchDouble([0,1,2,3,4,4,3,2,1])
#print len(contFrac(10001))

main(10000)
