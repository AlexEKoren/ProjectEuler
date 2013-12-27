def sP(n):
    if n%2==0:
        return 2
    for x in range(n-1,2,-1):
        if n%x==0:
            '''p=True
            for y in range(3,x):
                if x%y==0:
                    p=False
                    break
            if p==True:'''
            return x
    return 1
def exp(n):
    if n==1:
        return 1
    if n==2:
        return 1
    s=sP(n)
    if s==1:
        #print 2,n
        return exp(n-1)+1
    if s==2:
        #print 3,n
        return exp(n/2)+1
    if (n-s)%s==0:
        #print 4,n
        return exp(n-s)+1
    else:
        return exp(n-s)+exp(s)

t=0
for x in range(1,201):
    t+=exp(x)
print t
