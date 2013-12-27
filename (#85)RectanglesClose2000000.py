def main():
    x=1
    tris=[]
    while x<2000000:
        tris.append(x*(x+1)/2)
        x+=1
    print "done"
    x=3
    y=1
    m=2000000
    finalx=0
    finaly=0
    while m!=1 and y<2000000:
        temp=tris[y-1]
        #print "y=", temp, y
        while tris[x-3]*temp<2000000:
            #print "dhfoiwa"
            if abs(2000000-(tris[x-1]*temp))<m:
                m=abs(2000000-(tris[x-1]*temp))
                finalx=x
                finaly=y
                #print finalx, finaly, m
            x+=1
        y+=1
        x=3
    print m, finalx, finaly
    print finalx*finaly
main()
