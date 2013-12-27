import time
import fractions
def findFactors(n):
    x=[]
    #creates an array
    z=n
    if n!=1:
        x.append(z)
    if n==2:
        return 1
    #appends n and 1 to its factors
    y=z**.5
    #makes a variable that is one more than the square root of z
    p=2
    #starting value
    while p<=y:
        #continues until p is equal or greater than y
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            if not x.__contains__(p):
                x.append(p)
                temp=p
                temp2=p
                while temp+temp2<z:
                    temp+=temp2
                    if temp>z/2 and not x.__contains__(temp):
                        x.append(temp)
            if not x.__contains__(z/p):
                x.append(z/p)
        p=p+1
    #sorts the array
    #print len(x),x, n
    return len(x)

'''def reduced(a, b):
    #b is denominator
    if b%2==0 and a%2==0:
        return False
    if b%a==0:
        return False
    m=2
    while m<a/2:
        if b%m==0 and a%m==0:
            return False
        m+=1
    return True
    factors=findFactors(a)
    #print factors, a
    for l in factors:
        if b%l==0:
            return False
    return True'''

def main(z):
    t=time.time()
    x=2
    m=1
    counter=0
    while x<=z:
        y=findFactors(x)
        #print "counter plus: ",x-y
        counter+=x-y
        '''m=1
        while m<x:
            if reduced(m, x):
                counter+=1
                #print m,x
            m+=1'''
        x+=1
    t2=time.time()
    print t2-t
    print counter
            
main(10000)
