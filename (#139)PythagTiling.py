from math import *
from fractions import *
def pyth(m,n):
    return [m**2-n**2, 2*m*n, m**2+n**2]

def findTris(a):
    tris=[]
    for n in range(1,a):
        for m in range(n+1,a,2):
            if gcd(n,m)==1:
                temp=pyth(m,n)
                if sum(temp)>a:
                    break
                tris.append(temp)
    return tris

def main(l):
    total=0
    for i in range(1, l):
        for a in range(1, l):
            b=a+i
            if a+b>l:
                break
            aS=a**2
            bS=b**2
            s=aS+bS
            for c in range(b-a+i,l,i):
                if a+b+c>l:
                    break
                if s==c**2:
                    total+=1
                    print a, b, c
    print total
main(1000)
        
        
