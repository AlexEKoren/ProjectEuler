from itertools import *
from fractions import Fraction
from decimal import Decimal
def main(a):
    combs=[]
    for x in range(a/2+1,a+1):
        for y in combinations(range(a), x):
            combs.append(y)
    totalB=0
    totalR=1
    for x in combs:
        #print x
        if x==(0,2,3):
            continue
        temp=1
        for y in x:
            temp*=1.0/(y+2)
        #print temp
        totalR-=temp
        totalB+=temp
    print totalB, totalR
    print Fraction(Decimal(totalB))
main(4)
