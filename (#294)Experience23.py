import time
def d(k):
    t=0
    while k>0:
        t+=k%10
        k/=10
    return t
def main(a):
    t=time.time()
    count=0
    x=23
    while x<a:
        if d(x)==23:
            #print x, x/23
            count+=1
        x+=23*3
    print "10**"+str(a),count, time.time()-t

main(11**8)
