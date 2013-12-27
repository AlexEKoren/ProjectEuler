import time
from math import *
def pent(n):
    return n*(3*n-1)/2

def Xs(y):
    count=0
    x=1
    while x<y:
        if count%2==0:
            yield x
        else:
            yield -1*x
            x+=1
        count+=1
ps=[1,1]

def p(n):
    if n<len(ps):
        return ps[n]
    total=0
    count=1
    for x in Xs(n):
        if pent(x)>n:
            break
        sign=(-1)**(int((count-1)/2))
        total+=sign*p(n-pent(x))
        count+=1
    ps.insert(n, total)
    return total
    

print p(30)
