def check1(x,n):
    t=0
    for y in str(x):
        if int(y)==n:
            t+=1
    return t

def main():
    total=0
    t=0
    x=0
    while 1==1:
        t+=check1(x,4)
        if x==t:
            print "x:",x
            total+=x
            print "total:",total
        #if total==22786974071:
            #print x
        x+=1
main()
