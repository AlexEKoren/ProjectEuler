def checkBouncy(x):
    less=False
    more=False
    check=x%10
    x/=10
    while x>0:
        if x%10>check:
            more=True
        elif x%10<check:
            less=True
        check=x%10
        x/=10
    if more==True and less==True:
        return True
    return False

def main(a):
    total=0
    count=0
    m=0
    show=True
    for x in range(a):
        #print x
        m+=1
        #if x%10000==0:
            #print count, x
            #count=0
        '''if show==True and (m-total)*1.0/m>=.99:
            print x
            show=False'''
        if checkBouncy(x)==False:
            count+=1
            total+=1
        '''if x==9:
            print count
            count=0
        if x==99:
            print count
            count=0
        if x==999:
            print count
            count=0
        if x==9999:
            print count
            count=0
        if x==99999:
            print count
            count=0
        if x==999999:
            print count
            count=0
        if x==9999999:
            print count
            count=0'''
    print "non bouncy: ", total
    print "bouncy: ", m-total
    print "total: ", m
    print "percentage: ", total*100./m
main(1000000)
