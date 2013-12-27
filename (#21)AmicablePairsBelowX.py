#Finds all amicable pairs below x

def findFactors(n):
    x=[]
    #creates an array
    z=n
    y=z**.5+1
    p=1
    #makes a variable that is one more than the square root of z
    while p<y:
        #continues until y is 1
        if z%p==0:
            #if y is a factor of z it adds it and its opposite to the array
            x.append(p)
            if p!=1:
                x.append(z/p)
        p=p+1
    #x.sort()
    #print x
    return x

def d(n):
    a=findFactors(n)
    total=0
    for k in a:
        total+=k
    return total

def main(n):
    x=220
    total=0
    while x<n:
        if d(x)!=x and d(d(x))==x:
            print x
            total+=x
        x+=1
    print total

'''def main(x):
    total=0
    i=220
    j=1
    totalI=0
    totalJ=0
    k=0
    l=0
    while i<x:
        arrayI=findFactors(i)
        while k<(len(arrayI)):
            totalI=totalI+arrayI[k]
            k=k+1
        k=0
        while j<i:
            if j==i:
                j=j+1
            arrayJ=findFactors(j)
            while l<(len(arrayJ)):
                totalJ=totalJ+arrayJ[l]
                l=l+1
            l=0
            if totalJ==i and totalI==j:
                print i, j
                total=total+j+i
            j=j+1
            totalJ=0
        j=1
        i=i+1
        totalI=0
    print total'''

main(10000)
