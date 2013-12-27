def findFactors(x):
    f=[]
    for a in range(1,int(x**.5)+1):
        if x%a==0:
            f.append(a)
            if x/a!=a:
                f.append(x/a)
    f.sort()
    return f

def findFactorPairs(x):
    f=[]
    for a in range(1,int(x**.5)+2):
        if x%a==0:
            f.append([a,x/a])
            f.append([x/a,a])
    return f

def isSquare(x):
    s=x**.5
    if int(s)==s:
        return True
    return False


def P(f,r,s):
    if f==1:
        return r*(r+1)/2%10**8
    elif r==1:
        s=f
        s=s%10**8
        return s
    else:
        if f%2==0:
            odd=4*(f/2-1)+5
            even=2
            c=0
            while c<r-1:
                if c%2==0:
                    s+=odd
                    odd+=2
                else:
                    s+=even
                    even+=2
                c+=1
        else:
            odd=1
            even=4*(f/2-1)+6
            c=0
            while c<r-1:
                if c%2==0:
                    s+=odd
                    odd+=2
                else:
                    s+=even
                    even+=2
                c+=1
    return s%10**8
    
def main(a):
    f=findFactors(a)
    pairs=findFactorPairs(a)
    print "pairs done", len(pairs)
    floor=[]
    total=0
    for x in f:
        if x==1:
            floor.append([1,1])
        else:
            floor.append([x,(2*x**2+(-1)**x-1)/4])
    print "floors done", len(floor)
    #print P(10,20,50)
    for x in pairs:
        print x
        for y in floor:
            if x[0]==y[0]:
                fl=y[1]
                print fl
                break
        s=P(x[0],x[1],fl)
        total+=s
        total=total%10**8
    print total%10**8
    '''for n in range(2,a):
        inFloors=False
        for x in floor:
            if isSquare(x[-1]+n):
                x.append(n)
                inFloors=True
                break
        if inFloors==False:
            floor.append([n])
    print floor[9][19]'''

def main2(a):
    pairs=findFactorPairs(a)
    oddNext=5
    evenNext=4
    odd="33"
    even="2"
    s="1"
    
main(200000000)
#main(71328803586048)
            
