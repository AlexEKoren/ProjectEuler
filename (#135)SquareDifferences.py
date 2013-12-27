import time
def squares(x):
    s=[]
    for z in range(x+1):
        s.append(z**2)
    return s

def main(a):
    t=time.time()
    sq=squares(a)
    array=[0]*(a*2+1)
    for x in range(1,a):
        s=4*x
        for i in range(x/4,x):
            r=s*i-sq[x]
            if r>0 and r<a:
                if r==1155:
                    print x, i
                #print i , x
                array[r]+=1
                #print r
    print array.count(10), time.time()-t
    for x in range(a):
        if array[x]==10:
            print x
            1
main(10000)
