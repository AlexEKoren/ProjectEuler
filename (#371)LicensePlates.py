import itertools
import random
import time

def check(array, num):
    for x in range(len(array)):
        for y in range(x+1,len(array)):
            if array[x]+array[y]==num:
                return True
    return False

def main2(a, b):
    t=time.time()
    total=0
    f=0
    i=list(range(1000))
    print "list done"
    for x in range(a):
        array=[]
        count=0
        while check(array,10**b)==False:
            array.append(random.choice(i))
            count+=1
        total+=count
    print total*1.0/a
    
main2(127,3)
