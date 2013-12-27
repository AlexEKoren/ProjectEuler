def makeSquares(a):
    return [x**2 for x in range(1,int(a**.5)+1)]

def main(a):
    one=makeSquares(a)
    l=[[False,False,False,False] for x in xrange(a+1)]
    for o in one:
        for o2 in one:
            if o+7*o2<=a:
                l[o+o2][0]=True
                l[o+2*o2][1]=True
                l[o+3*o2][2]=True
                l[o+7*o2][3]=True
            elif o+3*o2<=a:
                l[o+o2][0]=True
                l[o+2*o2][1]=True
                l[o+3*o2][2]=True
            elif o+2*o2<=a:
                l[o+o2][0]=True
                l[o+2*o2][1]=True
            elif o+o2<=a:
                l[o+o2][0]=True
    total=0
    for n in range(len(l)):
        x=l[n]
        if not False in x:
            total+=1
            #print n,x
    print total

main(10000)
    
        
