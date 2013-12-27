from fractions import gcd
def check(e,n,mi):
    count=0
    for m in range(1,n):
        #print m
        if pow(m,e,n)==m:
            count+=1
            if count>mi:
                return n
    return count

def main(p,q):
    n=p*q
    mi=8
    tot=(p-1)*(q-1)
    total=0
    for e in range(2,tot-1):
        print e
        if gcd(e,tot)==1:
            #print e
            c=check(e,n,mi)
            if c<mi:
                total=e
                mi=c
                print "new", e, mi
            elif c==mi:
                print "next", e, mi
                total+=e
    print total

main(1009,3643)
