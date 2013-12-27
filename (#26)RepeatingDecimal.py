def main():
    x=1
    m=0
    final=0
    while x<1000:
        array=[]
        num=1
        while num<x:
            num*=10
        rem=num%x
        array.append(rem)
        if not rem%x==0:
            while rem<x:
                rem=rem*10
                #print "mhm"
        while not array.__contains__(rem%x):
            array.append(rem)
            if not rem%x==0:
                while rem<x:
                    rem*=10
                    #print "yep"
            rem%=x
        #print array, x
        if len(array)>m:
            final=x
            m=len(array)
        x+=1
    print final

main()
