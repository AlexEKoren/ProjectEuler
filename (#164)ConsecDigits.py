import time
counts = []
for x in range(10):
    counts.append([])
for x in counts:
    for y in range(10):
        x.append([])
for x in counts:
    for y in x:
        for z in range(20):
            y.append(0)

def rec(a,b,r):
    if r==0:
        return 1
    l = 9-a-b
    if (counts[a][b][r] == 0):
        for x in range(l+1):
            counts[a][b][r]+=rec(b,x,r-1)
    return counts[a][b][r]

def main():
    t=time.time()
    total=0
    for x in range(1,10):
        total+=rec(0,x,19)
    print total, time.time()-t

main()
