import time
def factor(n):  
    count=0
    if n%2==0:
        for y in range(2,int(n**.5)+1):
            if n%y==0:
                count+=1
                if n/y!=y:
                    count+=1
    else:
        for y in range(3, int(n**.5)+1,2):
            if n%y==0:
                count+=1
                if n/y!=y:
                    count+=1
    return count

def main(g):
    t=time.time()
    count=0
    c=0
    x=1
    temp=factor(x)
    temp2=factor(x+1)
    for a in range(1,g):
        while x<10**a:
            #print list(factor(x)),x
            if c%2==0:
                if temp==temp2:
                    print x, x+1
                    count+=1
                temp=factor(x+2)
            if c%2==1:
                if temp==temp2:
                    print x, x+1
                    count+=1
                temp2=factor(x+2)
            c+=1
            x+=1
        print time.time()-t
        print count

def main2(a):
    array=[]
    for x in range(10**a):
        array.append([x,0])
    l=10**a
    for y in range(2, l/2):
        i=y
        #print i
        while i<l:
            array[i][1]+=1
            i+=y
            #print i
    x=0
    count=0
    while x<len(array)-1:
        if array[x][1]==array[x+1][1]:
            #print array[x], array[x+1]
            count+=1
        x+=1
    print count-1    
main2(2)
