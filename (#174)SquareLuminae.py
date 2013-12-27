import time
def checkFit(t,x):
    total=0
    i=x+2
    while total<t:
        total+=i*2+(i-2)*2
        i+=2
    if total==t:
        #print x
        return True
    return False

def findL(t):
    total=0
    a=[]
    for x in range(1,t/4):
        if checkFit(t,x):
            a.append(x)
            total+=1
    #if len(a)>=3:
        #print t, a
    return total

def findL2(t):
    total=0
    for x in range(1,t/4):
        if (t+x) in array:
            total+=1
    return total

def findL3(t):
    total=1
    b=False
    y=2
    while 1:
        temp1=4*y**2
        if t-temp1<4*y:
            break
        temp=(t-temp1)/(4.*y)
        if temp==int(temp):
            total+=1
        y+=1
    return total

def main(a,n,b,p):
    d=time.time()
    Ls=[0]*(a+1)
    for t in range(8,a+1,4):
        Ls[t]=findL3(t)
        #print t, Ls[t]
    total=0
    if p==True:
        print sum(Ls), time.time()-d
        return
    else:
        for t in range(len(Ls)):
            if b==False:
                if Ls[t]<=n and Ls[t]!=0:
                    total+=1
            else:
                if Ls[t]==n:
                    total+=1
        print total,time.time()-d

main(10000,10,False,True)
            
