from fractions import *
def fractions(a):
    count=1
    for x in xrange(a+1,2*a):
        #print x
        num1=1
        denom1=a
        num2=1
        denom2=x
        num1*=denom2
        num2*=denom1
        denom1,denom2=(denom1*denom2),(denom1*denom2)
        num2=num1-num2
        #print num2, denom2
        if denom2%num2==0:
            count+=1
    return count

def fractions2(a):
    num=a**2
    count=0
    for x in range(1,a+1):
        if num%x==0:
            count+=1
    return count
                

def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)

def checkD(n,a):
    for x in range(2,a+1):
        if n%x!=0:
            return False
    return True

def findI(a):
    x=factorial(a)
    for y in range(2,a):
        while checkD(x,a):
            x/=y
        x*=y
    return x

def main(a):
    x=0
    i=findI(17)#findI(20)
    print "found"
    m=0
    temp=0
    while temp<a:
        x+=i
        print x
        temp=fractions2(x)
        #print x, temp
        if temp>m:
            print x, temp
            m=temp
    print x

main(10000)
