def findGeo(n):
    for d in range(2,n):
        q=n/d
        r=n%d
        if r!=0:
            if d*1./q==q*1./r:
                print 1, n, q, r, d
                return n
            if d*1./r==r*1./q:
                print 2, n, q, r, d
                return n
            if q*1./d==d*1./r:
                print 3, n, q, r, d
                return n
    return 0

def main(a):
    total=0
    for x in range(a):
        #print x
        total+=findGeo(x**2)
    print total

main(105)
