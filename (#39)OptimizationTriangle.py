def main():
    array=[]
    x=0
    p=0
    final=0
    while x<5000:
       array.append(0)
       x=x+1
    a,b=1,1
    while a<=1000:
        while b<=1000:
            c=(a**2+b**2*1.0)**.5
            if c%1==0:
                #print c
                d=int(a+b+c)
                #print d
                r=array[d-1]
                array[d-1]=r+1
                #print array[d-1]
                #print "array changed"
            b=b+1
        b=a
        a=a+1
    while p<len(array):
        q=array[p]
        print q,p
        if q>final:
            final=p
        p=p+1
        
    print final
            
main()
