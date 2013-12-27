from math import *
from fractions import *
def findR(a,b,c):
    s=(a+b+c)/2
    #print s, a, b, c
    return 1.0*(s-a)*(s-b)*(s-c)/s

def findXY(l, theta):
    x=l*cos(radians(theta))
    y=l*sin(radians(theta))
    return x, y

def main(l):
    count=0
    for a in range(l**2):
        for b in range(1,a):
            fA=findXY(a, 60)
            fB=findXY(b, 0)
            c=sqrt((fA[1]-fB[1])**2+(fA[0]-fB[0])**2)
            if int(c)==c:
                r=findR(a,b,c)
                #print r
                if sqrt(r)>l:
                    break
                else:
                    count+=1
    print count

def main2(l):
    count=0
    limit=l**2
    for m in range(1,l):
        for n in range(m):
            if gcd(m, n)==1:
                a=m**2-m*n+n**2
                b=2*m*n-n**2
                c=m**2-n**2
                if a!=0 and b!=0 and c!=0:
                    print a, b, c, m, n
                    G1=gcd(a,b)
                    G2=gcd(a,c)
                    if G1==G2:
                        a/=G1
                        b/=G1
                        c/=G1
                        aI=a
                        bI=b
                        cI=c
                        r=findR(a,b,c)
                        while r<limit:
                            count+=1
                            a+=aI
                            b+=bI
                            c+=cI
                            r=findR(a,b,c)
                    #print a, b, c
                    else:
                        r=findR(a,b,c)
                        if r<limit:
                            count+=1
                        else:
                            break
    print count
main2(100)
