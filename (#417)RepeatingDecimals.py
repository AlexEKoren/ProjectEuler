def repeat(n):
    #print n
    rs=[]
    r=1
    d=0
    while not r in rs[:-1] and r!=0:
        if r>n:
            d=r/n
            r=r%n
            rs.append(r)
        else:
            r*=10
    if r!=0 and rs.count(r)>1:
       # print rs.count(r)
        i1=rs.index(r)
        i2=rs[i1+1:].index(r)+i1+1
        return i2-i1
    return 0

def main(l):
    s=0
    for x in range(1,l):
        s+=repeat(x)
    print s

main(10000)
