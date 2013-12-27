import itertools

def main(a):
    i=itertools.product(range(26), repeat=a)
    count=0
    total=0
    for x in i:
        total+=1
        #print x
        b=False
        y=0
        while y<len(x)-1:
            if x[y+1]-x[y]==1:
                if b==True:
                    b=False
                    break
                b=True
            y+=1
        if b==True:
            #print x
            count+=1
    print count, total

def iterate(a):
    array=[]
    for x in a:
        if x[0]==False:
            x.append(x[1]+1)
            x[0]=True
            array.append(x)
        else:
            for y in range(26):
                if y!=x[-1]+1:
                    array.append(x+[y])
    return array
def main2(a):
    array=list([False,x] for x in range(26))
    n=10234498
    for y in range(a):
        array=iterate(array)
        print len(array)
        
    
    
main2(5)
