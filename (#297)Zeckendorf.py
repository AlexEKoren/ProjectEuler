import time
def fibs(l):
    a=1
    b=1
    f=[]
    while b<l:
        f.append(b)
        a,b=b,a+b
    f.append(b)
    return f

a=1000000
fib=fibs(a)
print len(fib)

def findHighest(x):
    i=0
    while fib[i]<x:
        i+=1
    return fib[i-1]

def findZ(x):
    if not x in fib:
        return 1+findZ(x-findHighest(x))
    else:
        return 1

def main(a):
    t=time.time()
    count=0
    for x in xrange(1,a):
        count+=findZ(x)
    print time.time()-t,count

main(a)

        
