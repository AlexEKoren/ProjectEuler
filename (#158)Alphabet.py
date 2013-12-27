def main(a):
    prev=[]
    for x in range(1,27):
        prev.append([x,26-x])
    print prev
    for n in range(3,a+1):
        for x in range(1,27):
            up=0
            for y in range(26*(n-3),26*(n-2)):
                if prev[y][0]>x:
                        up+=prev[y][1]+1
            nex=[x,up]
            prev.append(nex)
        print prev[26*(n-3):26*(n-2)]
    m=0
    num=0
    for n in range(3,a+1):
        count=0
        for x in range(26*(n-3),26*(n-2)):
            count+=prev[x][1]
        if count>m:
            m=count
            num=n
    print count, num

main(26)

