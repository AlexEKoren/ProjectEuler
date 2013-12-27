import math
from decimal import *
from time import time
getcontext().prec=100
def contFrac(x):
    rootX=Decimal(x)**Decimal('0.5')
    #print rootX
    f=[int(Decimal(x)**Decimal('0.5'))]
    temp=rootX-int(rootX)
    while f[0]*2!=f[-1]:
        #print f
        temp=Decimal(1)/Decimal(temp)
        f.append(int(temp))
        temp=(temp-int(temp))
    #print len(f)
    return f

def convertContFrac(f):
    #print f
    f=f[:-1]
    #print f
    if (len(f)-1)%2==0:
        #print f
        f=f[0:]+[2*f[0]]+f[1:]
    #print f
    num=1
    denom=f[-1]
    #print f[1:-1]
    for x in reversed(f[1:-1]):
        #print x
        num=x*denom+num
        denom,num=num,denom
        #print num, denom
    #print num, denom
    num+=f[0]*denom
    return num, denom

def main(a):
    t=time()
    m=0
    final=0
    for D in range(a+1):
        if D**.5==int(D**.5):
            continue
        temp=convertContFrac(contFrac(D))
        if long(temp[0]**2)-D*long(temp[1]**2)==1:
            #print D, len(str(temp[0]))
            if temp[0]>m:
                    m=temp[0]
                    final=D
                    print "D:", D
    print final, time()-t


#convertContFrac(contFrac(989))
main(1000)
