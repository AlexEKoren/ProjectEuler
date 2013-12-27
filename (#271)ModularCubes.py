import math
import itertools
f=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
subsets=lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
sub=subsets(f)
sub.remove([])

def checkQuad(a,b,c):
    if b**2-4*a*c<0:
        return 0
    top1,top2=b*-1,b*-1
    sq=math.sqrt(b**2-4*a*c)
    if sq.is_integer():
        top1+=sq
        top2-=sq
    top1/=2*a
    top2/=2*a
    if top1>=0:
        if top1.is_integer():
            return top1
    elif top2>=0:
        if top2.is_integer():
            return top2
    return 0

def mul(s):
    t=1
    for x in s:
        t*=x
    return t

def main(n):
    print int(n)
    total=0
    for x in sub:
        m=mul(x)
        if checkQuad(1,1,1-m)!=0:
            xR=checkQuad(1,1,1-m)
            temp=[]
            for y in f:
                if not y in x:
                    temp.append(y)
            xL=mul(temp)+1
            print long(xR*xL)
def main2(n):
    for x in range(10000):
        l=x*n+1
        
        
main(13082761331670030)
