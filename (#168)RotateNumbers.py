import math
import time
def rotate(x):
    l=int(math.log10(x))
    temp=int(x/10**l)
    x%=10**l
    x*=10
    x+=temp
    return x

'''def main(a):
    t=time.time()
    total=0
    x=10
    while x<a:
        if x%rotate(x)==0:
            temp=x
            while temp<10**(int(math.log10(x))+1):
                total+=temp
                temp+=x
                #print temp, x
        x+=1
        if math.log10(a)-int(math.log10(a))>.04575748621773:
            x=10**(math.log10(a)+1)
    print total, time.time()-t

main(1000000)'''

def main2(a):
    t=time.time()
    total=0
    for x in range(10,a):
        if x%rotate(x)==0:
            total+=x
            #print x
    print total, time.time()-t

main2(10000000)
