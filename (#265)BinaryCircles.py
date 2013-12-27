import itertools
def makeSubsets(n):
    return itertools.product(range(2),repeat=n)

def extendSets(l,s,n):
    new=[]
    for x in l:
        #print "x: ",x
        temp=x[-2:]
        for y in s:
            #print "x: ", x, x[-2:], "y: ", y, y[:n-1]
            if y[:n-1]==temp:
                #print "yes", x+y[-1:]
                new.append(x+y[-1:])
    return new

def main(n):
    s=makeSubsets(n)
    pres=list(makeSubsets(n))
    new=extendSets(pres,pres,n)
    print new
    while len(new[0])!=2**n:
        pres=new
        new=extendSets(pres,pres,n)
        print len(new[0])
    print pres

main(3)

