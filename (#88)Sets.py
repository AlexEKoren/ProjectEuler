import time, math
def mul(s):
    t=1
    for x in s:
        t*=x
    return t

def findAllFactors(limit):
    ml=int(math.log(limit,2)-1)
    f=[1 for x in range(ml)]
    f[0]=1
    final=[[x] for x in range(2,limit+1)]
    used=1
    x=0
    while True:
        if x==0:
            if used==ml:
                break
            if f[0]<f[1]:
                f[0]+=1
            else:
                used+=1
                f[used-1]=2*limit+1
                f[0]=2
            x+=1
            f[1]=f[0]-1
        elif x==used-1:
            f[x]+=1
            if mul(f)>2*limit:
                x-=1
            else:
                final.append(f[:used])
        elif f[x]<f[x+1]:
            f[x]+=1
            f[x+1]=f[x]-1
            x+=1
        elif f[x]>=f[x+1]:
            x-=1
    return final
        

def factor2(a):
    t=time.time()
    factors=findAllFactors(a)
    allNums=[2*(a+1) for x in range(a+1)]
    limit=2*a+1
    for x in factors:
        dif=mul(x)-sum(x)
        if len(x)+dif<=a:
            if allNums[len(x)+dif]>mul(x):
                allNums[len(x)+dif]=mul(x)
    allNums[0]=0
    allNums[1]=0
    print sum(set(allNums)), time.time()-t

factor2(12000)
