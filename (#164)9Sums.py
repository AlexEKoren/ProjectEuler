def main(a):
    prev=[]
    for x in range(1,10):
        prev.append([x,10-x])
    print prev
    for n in range(3,a+1):
        nex=[[x,0] for x in range(1,10)]
        for x in range(1,10):
            for y in range(9*(n-3),9*(n-2)):
                if prev[y][0]+x<=9:
                    #print prev[y][0]+x
                    nex[prev[y][0]+x-1][1]+=prev[y][1]+1
            prev+=nex
        print prev[9*(n-3):9*(n-2)]
    print sum(x[1] for x in prev[-9:])
    #print prev[-9:]
main(20)

