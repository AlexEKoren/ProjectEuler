import time
def main(x):
    t=time.time()
    fib=[]
    m=0
    b=False
    for y in range(2000):
        fib.append(1)
    for y in range(2000,x+1):
        fib.append(fib[y-2000]+fib[y-1999])
        if fib[-1]!=m:
            #print fib[-1], y
            m=fib[-1]
            if y%2000==0 and m!=(2**(y/2000)):
                #b=True
                print y, m%20092010
                fib.pop(0)
            #if b==True:
                #if y%2000==0 and m==(2**(y/2000)-2):
                    #print y, m
        #print len(fib)
        #print fib[-1], y
        #if y>5000:
            #fib.pop(0)
        
    print fib[-1]%20092010, time.time()-t
main(10000000)
