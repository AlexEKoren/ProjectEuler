import time
def main(a):
    prev=[]
    for x in range(1,10):
        prev.append([x,9-x,x])
    for n in range(3,a+1):
        for x in range(1,10):
            up=0
            down=1
            for y in range(9*(n-3),9*(n-2)):
                if prev[y][0]<x:
                        down+=prev[y][2]+1
                elif prev[y][0]>x:
                        up+=prev[y][1]+1
                else:
                    down+=prev[y][2]
                    up+=prev[y][1]
            nex=[x,up,down]
            prev.append(nex)
    print sum(sum(x[1:])+1 for x in prev)+9
t=time.time()
main(10**3)
print time.time()-t
