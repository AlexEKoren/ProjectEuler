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
    return str(p)

def main():
    total=0
    for x in range(1,101):
        if not (int(x**.5))**2==x:
            s=sqrt(x)
            print s
            if len(s)<100:
                s=list(s)
                total+=sum(s)
            for y in range(100):
                total+=int(s[y])
    print total
        
main()
