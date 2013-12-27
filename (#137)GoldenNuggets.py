from math import sqrt
def fib(a):
    f=[0,1,1]
    b=1
    c=1
    while c<a:
        b,c=c,b+c
        f.append(c)
    return f

def isInt(x):
    #print x, round(x)
    if abs(x-round(x))<.00001 and x>1 and x<100000000000:
        return True
    return False

def main(a):
    nuggets=[]
    fibs=fib(a)
    for x in range(1,len(fibs)):
        s=sqrt(fibs[x])
        for y in range(x):
            if fibs[y]>s:
                break
            else:
                for d in fibs[1:]:
                    m=(s-fibs[y])/d
                    #print fibs[x], fibs[y], d
                    #print "m",m
                    total=0
                    if abs(m)<1:
                        for z in range(1,len(fibs)):
                            total+=(m**z)*fibs[z]
                        if isInt(total):
                            print fibs[x], fibs[y], d, long(round(total))
                            nuggets.append(long(round(total)))
                        #print m, fibs[x], fibs[y], fibs[x-y], total
        m=1./fibs[x]
        total=0
        if m<1:
            for z in range(1,len(fibs)):
                total+=(m**z)*fibs[z]
            if isInt(total):
                print fibs[x], total
                nuggets.append(long(round(total)))
    nuggets=list(set(nuggets))
    nuggets.sort()
    
    print nuggets[:16]
    

main(10000000000000000000000000000000)
