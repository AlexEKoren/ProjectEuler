import time
def findSquares(x):
    s=[]
    for y in range(x):
        s.append(y**2)
    return s

def factor(x):
    f=[1]
    for y in range(2,int(x**.5)+1):
        if x%y==0:
            f.append(y**2)
            f.append((x/y)**2)
    return list(set(f))

def main(x):
    t=time.time()
    s=findSquares(1000)
    total=0
    for y in range(1, x):
        f=factor(y)
        z=0
        if s.__contains__(sum(f)):
            print y, f, sum(f)
            total+=y
    print total
    print time.time()-t
main(1000)
