import time
import fractions
def M(x):
    m=0
    final=1
    for y in range(x/3+1,x/2+1):
        temp=(x*1.0/y)**(y/100.)
        if temp>m:
            m=temp
            final=y
        elif temp<m and m!=0:
            break
    #print m, x
    return final

def reducefract(n, d):
    greatest=fractions.gcd(n,d)
    d/=greatest
    return d

#reducefract(6,10)

def checkTerm(d):
    while d%2==0:
        d/=2
    while d%5==0:
        d/=5
    if d!=1:
        return False
    return True
        
#print checkDiv(1,4)
def main(a):
    t=time.time()
    total=0
    for x in range(1,a+1):
        #print x
        temp=M(x)
        #print temp, x
        denom=reducefract(x, temp)
        #print frac
        if checkTerm(denom):
            #print "Yes", x
            #print x
            total-=x
        else:
            total+=x
    print total, time.time()-t

main(10000)
