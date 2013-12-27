def rec(depth,n):
    if depth==3:
        return 1
    if n==0:
        #print n, rec(depth+1,0)+rec(depth+1,1)+rec(depth+1,2)+rec(depth+1,3)
        return rec(depth+1,0)+rec(depth+1,1)+rec(depth+1,2)+rec(depth+1,3)
    if n==1:
        #print n, (rec(depth+1,0)+rec(depth+1,1)+rec(depth+1,2))
        return rec(depth+1,0)+rec(depth+1,1)+rec(depth+1,2)
    if n==2:
        #print n,rec(depth+1,0)+rec(depth+1,1)
        return rec(depth+1,0)+rec(depth+1,1)
    if n==3:
        #print n, rec(depth+1,0)
        return rec(depth+1,0)

#print rec(0,1)
#print rec(0,2)
#print rec(0,3)

def rec2(depth,n):
    if depth==15:
        return 1
    return sum((rec2(depth+1,x) for x in range(9-n)))

print list((rec2(0,x) for x in range(1,9)))


