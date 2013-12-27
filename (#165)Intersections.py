def gen():
    s=290797
    while 1:
        s=s**2%50515093
        yield s%500

def lcm(a,b):
    return a*b

def main(a):
    g=gen()
    lines=[]
    points=set([])
    for x in range(a):
        x1=g.next()
        y1=g.next()
        x2=g.next()
        y2=g.next()
        n=y2-y1
        d=x2-x1
        if d==0:
            continue
        b=y1-n*1./d*x1
        lines.append((n,d,b))
    for x in range(len(lines)):
        for y in range(x+1,len(lines)):
            l1=lines[x]
            l2=lines[y]
            b1,b2=l1[2],l2[2]
            n1,n2=l1[0],l2[0]
            d1,d2=l1[1],l2[1]
            b1*=d2
            b2*=d2
            n1*=d2
            b1*=d1
            b2*=d1
            n2*=d1
            n1-=n2
            b2-=b1
            if n1==0:
                continue

            x3=b2*1./n1
            y3=n1*1./d1*x+b1
            points.add((x3,y3))
    print len(points)

main(100)
