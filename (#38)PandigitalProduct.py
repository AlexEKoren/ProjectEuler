import itertools
def main():
    perms1=list(itertools.permutations([9,8,7,6,5,4,3,2,1]))
    #print perms[0]
    perms=[]
    for l in perms1:
        sub=""
        for p in l:
            sub+=str(p)
        perms.append(sub)
        #print sub
    #print perms
    final=0
    x=1
    while x<100000/2:
        #print x
        n=1
        strX=""
        while len(strX)<9:
            strX+=str(x*n)
            n+=1
        if len(strX)==9:
            #print strX, x
            if perms.__contains__(strX):
                print "yep"
                if int(strX)>final:
                    final=int(strX)
                    print final,x
        x+=1
    print final
main()
