def main(a,i,xi,ii):
    m=0
    mx=0
    mi=0
    b=False
    while i<.2:
        x=.1
        while x<.3:
            temp=x
            t=1
            for y in range(0,5):
                t*=temp**(y+1)
                temp+=i
            temp-=i
            #print temp
            temp=2-temp
            #print temp
            for y in range(5,10):
                t*=temp**(y+1)
                temp+=i
            #print temp-i
            #print x, i, t, xi, ii
            x+=xi
            if t>m:
                m=t
                mx=x
                mi=i
        i+=ii
    print m, mx, mi

main(10,.15,.02,.00001)
