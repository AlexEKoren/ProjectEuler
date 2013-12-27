from decimal import Decimal
def sqrt(a):
    p=0
    e=str(a)
    e=list(e)
    if e.__contains__("."):
        e.remove(".")
    s=""
    for z in e:
        s+=z
    if len(s)%2==1:
        s="0"+s
    print s
    for y in range(200):
        s+="00"
    b=0
    c=2
    temp=int(s[b:c])
    for x in range(150):
        #print temp
        c,b=c+2,b+2
        x=1
        while (20*p+x)*x<=temp:
            x+=1
        x-=1
        temp=int(str(temp-(20*p+x)*x)+s[b:c])
        p=int(str(p)+str(x))
    return p


def check9(x):
    c=0
    while c<len(x)-1:
        if x[c]!=x[c+1]:
            return False
    return True
        

def main(a):
    total=0
    for p in range(2,a):
        rP=sqrt(p)
        print rP
        for q in range(p+1, a+1):
            l=1
            if p+q>2011:
                break
            y=2
            qP=sqrt(q)
            z=(rP+qP)**y
            while len(str(z))<a:
                z=(rP+qP)**y
                y+=2
                l+=1
            while check9(str(z)[l:a])==False:
                z=(rP+qP)**y
                y+=1
                l+=1
            print str(z), y
            total+=y
    print total

main(5)


                
