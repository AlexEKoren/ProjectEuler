import time
def findFactors(n):
    x=[]
    #creates an array
    z=n
    x.append(1)
    y=z**.5
    p=2
    #makes a variable that is one more than the square root of z
    while p<=y:
        #continues until y is 1
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            if z/p!=p:
                x.append(z/p)
            x.append(p)
            p=p+1
        else:
            p=p+1
    #print x
    return x

def findAbundants(x):
    abundants=[]
    i=12
    subtotal=0
    while i<x:
        l=findFactors(i)
        for m in l:
            subtotal=subtotal+m
        if subtotal>i:
            abundants.append(i)
        i=i+1
        subtotal=0
    #print abundants
    return abundants


def main(x):
    abuns=findAbundants(x)
    #print abuns
    total=0
    array=[]
    array2=[]
    for i in abuns:
        for j in abuns:
            if i+j<x:
                array.append(i+j)
    print "added all", len(array)
    array=list(set(array))
    print len(array)
    print "deleted doubles"
    for x in range(1,28123):
        if x not in array:
            total+=x
            #print total
            #print x
    print total
    '''total=0
    s=0
    for x in range(28124):
        s+=x
    for x in array:
        total+=x
    for x in range(28124):
        if x not in array:
            array2.append(x)
    for l in array2:
        for k in array2:
            if 10533-k-l in array2:
                print k, l, 10533-k-l
    print s-total, "final"'''


main(28123)
            



                              
