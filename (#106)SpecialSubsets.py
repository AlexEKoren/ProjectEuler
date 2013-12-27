import itertools
import time
def main(a):
    t=time.time()
    array=range(a)
    count=0
    total=0
    size=2
    while size<=a/2:
        for i in itertools.combinations(array,size):
            for j in itertools.combinations(array,size):
                    if len([x for x in i if x in j])==0:
                        total+=1
                        up=False
                        down=False
                        for x in range(size):
                            if i[x]>j[x]:
                                up=True
                            else:
                                down=True
                        if up and down:
                            count+=1
                            #print i, j
                        
        size+=1
    print count/2, time.time()-t
    
main(12)
        
