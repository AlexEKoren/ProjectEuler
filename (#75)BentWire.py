import time
from math import *
from fractions import *
def tri(m, n):
    #print m**2-n**2, 2*m*n, m**2+n**2
    return [m**2-n**2, 2*m*n, m**2+n**2]

def main(x):
    array=[0]*(x+1)
    t=time.time()
    for m in range(2,int(x**.5)):
        #print m
        for n in range(1, m):
            if n==m:
                continue
            a=tri(m,n)
            if gcd(a[0],a[1])==1 and gcd(a[0],a[2])==1:
                #print a
                s=sum(a)
                i=sum(a)
                while s<=x:
                    array[s]+=1
                    s+=i
    count=0
    y=2
    while y<len(array):
        if array[y]==1:
            #print y
            count+=1
        y+=1
    print count, time.time()-t

def main2(l):
    count=0
    for x in range(1,l+1):
        #print x
        temp=0
        for c in range(1,x):
            for b in range(1, c):
                a=x-c-b
                if a<b:
                    break
                if a**2+b**2==c**2:
                    temp+=1
        #print x, temp
        if temp==1:
            print x
            count+=1
    print count
main(1500000)

