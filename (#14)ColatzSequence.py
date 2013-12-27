import time
def iterate(x):
    count=0
    while x!=1:
        if x%2==0:
            x/=2
        else:
            x=x*3+1
        count+=1
    return count

def main(a):
    t=time.time()
    m=0
    mx=0
    for x in range(1,a,2):
        i=iterate(x)
        if i>m:
            #print x, m
            m=i
            mx=x
    print mx, time.time()-t

main(1000000)
