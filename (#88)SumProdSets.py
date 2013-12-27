from itertools import combinations

def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def lcmm(a):
    return reduce(lcm, a)

def mul(s):
    return len(s)==1 and s[0] or s[0]*mul(s[1:])

def check(n):
    factors=[]
    x=2
    while x<=n:
        while n%x==0:
            factors.append(x)
            n/=x
        x+=1
    pos=list(combinations(factors,len(factors)-1))
    if len(pos)<=1:
        return False
    muls=[]
    for x in pos:
        muls.append(mul(x))
    l=lcmm(muls+[mul(factors)])
    fracs=[]
    for x in muls:
        fracs.append([l/x,l])
    #print fracs
    total=sum(x[0] for x in fracs)
    dif=l-total
    return len(factors)+dif
    
def main(a):
    l=[0 for x in range(a+1)]
    for x in range(4,a*2):
        index=check(x)
        if index<=a:
            if l[index]>x or l[index]==0:
                l[index]=x
        for y in range(2,min(a+1,index)):
            if l[y]>x or l[y]==0:
                l[y]=x
    #print l
    print sum(set(l))-5
    print l[-1]

main(500)



        
        
