import random
def main(w):
    final1=0
    final2=0
    for x in range(1000000):
        p1=0
        p2=0
        go3=False
        while p1<100 and p2<100:
            add=True
            r=int(random.random()*2)
            if r==1:
                #print p1
                p1+=1
            #m=int(random.random()*2)
            for y in range(w):
                r=int(random.random()*2)
                if r!=1:
                    add=False
                    break
            if add==True:
                p2+=2**(w-1)
                if go3==True:
                    w=3
                else:
                    w=6
                go3=True
        #print p1>p2, p1, p2
        if p1>p2:
            final1+=1
        else:
            final2+=1
    print "T="+str(w)
    print "final 1: "+str(final1)
    print "final 2: "+str(final2)

#main(1)
#main(2)
#main(3)
#main(4)
#main(5)
#main(6)
main(7)
#main(8)
#main(9)
