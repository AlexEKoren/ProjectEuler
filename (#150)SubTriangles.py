def rands():
    t=0
    ex=2**20
    ex2=2**19
    for x in range(500500):
        t=(615949*t + 797807)%ex
        yield t-ex2

def makeTri():
    l=1
    tri=[]
    temp=[]
    count=0
    for y in rands():
        temp.append(y)
        count+=1
        if count==l:
            l+=1
            tri.append(temp)
            temp=[]
            count=0
    return tri

def main():
    tri=makeTri()
    m=0
    for y in reversed(range(len(tri))):
        print y
        for x in range(y+1):
            s=0
            for dy in range(y):
                s+=sum(tri[dy][x:x+dy+1])
                if s<m:
                    m=s
                    print m                
    print m
main()
