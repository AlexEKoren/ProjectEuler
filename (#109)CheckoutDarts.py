import time
def main(a):
    t=time.time()
    count=0
    muls=[[1],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]
          ,[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]
          ,[1,2,3],[1,2,3],[1,2,3],[1,2,3],[],[],[],[],[1,2]]
    for x in (range(21)+[25]):
        for y in (range(x,21)+[25]):
            for z in (range(1,21)+[25]):
                for m1 in muls[x]:
                    for m2 in muls[y]:
                        if x==y:
                            if m1<=m2:
                                if m1*x+m2*y+2*z<a:
                                    count+=1
                        else:
                            if m1*x+m2*y+2*z<a:
                                count+=1
    print count, time.time()-t
    return count

print main(100)
