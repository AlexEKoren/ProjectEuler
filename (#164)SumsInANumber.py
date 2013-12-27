import itertools
def main(a):
    permstemp=list(itertools.product(range(10), repeat=3))
    perms3=[]
    for x in permstemp:
        if sum(x)>9:
            perms3.append(x) 
    perms=list(itertools.product(range(10), repeat=a))
    print len(perms)
    count=0
    for x in perms:
        if x[0]==0:
            continue
        print x, count
        b=False
        for y in perms3:
            #print y
            if y in x:
                b=True
                print "yes"
                break
        if b==False:
            count+=1
    print count

main(4)
    
