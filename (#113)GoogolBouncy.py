import math
def increasing(x):
    while x%10>(x/10%10):
        if x==0:
            return True
        x/=10
    return False

def decreasing(x):
    while x%10<(x/10%10):
        x/=10
        if x<10:
            return True
    return False

def same(x):
    while x%10==(x/10%10):
        x/=10
        if x<10:
            return True
    return False

def isBouncy(x):
    up=False
    down=False
    temp=x
    temp2=x
    while x/10>0:
        if x%10>x/10%10:
            up=True
        if x%10<x/10%10:
            down=True
        if up and down:
            return True
        x/=10
    '''while temp>0:
        if temp%10==temp/10%10 and temp/10<10:
            return True
        elif temp%10!=temp/10%10:
            return False
        temp/=10'''
    return False

def main(a):
    i=0
    d=0
    s=0
    temp=0
    for x in range(1,10**a+1):
        if math.log(x,10)==int(math.log(x,10)) or x==1000 or x==1000000:
            print str(x)+": ",(i+d+s), temp/2, temp, (temp-11)/2
            temp=0
            if x==10**a:
                break
        if not isBouncy(x):
            i+=1
            temp+=1
        '''if increasing(x):
            i+=1
            temp+=1
        elif decreasing(x):
            d+=1
            temp+=1
        elif same(x):
            s+=1'''
    print i+d+s

def tri(n):
    return n*(n+1)/2

def main2(l):
    total=99
    temp=0
    a=0
    d=0
    s=0
    for x in range(1,int(10**(l-2)+1)):
        if math.log(x,10)==int(math.log(x,10)) or x==1000 or x==1000000:
            print total, str(x)+": ",(a+d+s), temp/2, temp, (temp-11)/2
        if same(x):
            if increasing(x):
                total+=tri(10-x%10-1)
                a+=tri(10-x%10-1)
            if decreasing(x):
                total+=tri(x%10)
                d+=tri(x%10)
            s+=1
            total+=1
        else:
            if increasing(x):
                total+=tri(10-x%10)
                a+=tri(10-x%10)
            if decreasing(x):
                total+=tri(x%10+1)
                d+=tri(x%10+1)
main2(6)        
        
