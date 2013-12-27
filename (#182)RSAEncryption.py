from fractions import *
def main(p,q):
    n=p*q
    tot=(p-1)*(q-1)
    minimum=10**100
    total=0
    for e in range(2,tot):
        if gcd(e,tot)==1:
            count=0
            for m in range(n):
                if m**e%n==m:
                    count+=1
                    print e, m
            if count<minimum:
                minimum=count
                total=1
                print e, count
            elif count==minimum:
                total+=1
                print e, count
    print total

main(1009,5)
