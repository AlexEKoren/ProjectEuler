def main(x):
    total=0
    for a in range(3,x+1):
        m=0
        num=0
        sq=a**2
        low=(a-1)
        high=(a+1)
        for n in range(1,3*a):
            l=(low+high)%sq
            #print a, n, l
            if l>m:
                m=l
                num=n
            low*=a-1
            high*=a+1
        print "final",a, m, num
        total+=m
    print total
main(1000)
