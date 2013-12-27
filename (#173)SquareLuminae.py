import time
def main(a,n):
    t=time.time()
    Ls=[0]*(a+1)
    for i in range(1,a):
        d=i+2
        o=d**2-i**2
        while o<=a:
            Ls[o]+=1
            d+=2
            o=d**2-i**2
    print sum(Ls), time.time()-t

main(1000000,10)
