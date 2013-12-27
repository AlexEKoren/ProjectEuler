import math
import time
from fractions import gcd
def isSq(x):
    return math.sqrt(x).is_integer()    

def isIntPyth(a,b):
    return isSq(a**2+b**2)

def mid(a,b,c):
    l=[a,b,c]
    l.sort()
    return l[1]

def genPyth():
    m=1
    while 1:
        for n in range(1,m):
            if gcd(m,n)==1:
                yield (m**2-n**2,2*m*n)
        m+=1

def main(limit):
    t=time.time()
    count=0
    x=2
    a,b=1,1
    while count<limit:
        while a<=x:
            while b<=a:
                if isIntPyth(a,b):
                    count+=-a+b+1+int(a/2)
                b+=1
            a+=1
            b=1
        x+=1
        #print x, count
    print a
main(1000000)
    
