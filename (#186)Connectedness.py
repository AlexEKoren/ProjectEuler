import math
from time import time
def gen():
    array=[]
    for x in range(1,56):
        array.append((100003-(200003*x)+(300007*(x**3)))%1000000)
        yield (100003-(200003*x)+(300007*(x**3)))%1000000
    y=56
    while 1:
        #print y-56, len(array), y-25
        array.append((array[y-25]+array[y-56])%1000000)
        yield (array[y-25]+array[y-56])%1000000
        if array[-1]==524287:
            print y
        #if y==3681161:
            #print (array[-25]+array[-56])%1000000
        #if y==3681162:
            #print (array[-25]+array[-56])%1000000
        y+=1
        #print array
        '''if y==3681162:
            print (array[y-26]+array[y-57])%1000000'''

nums=[[i] for i in range(10**l)]
def isInt(x):
    try:
        x+=1
    except TypeError:
        return False
    return True

def findPos(x):
    i=x
    while isInt(nums[i]):
        i=nums[i]
    return i

def main(l):
    PM=524287
    t=time()
    global nums
    #print nums
    g=gen()
    count=0
    m=1
    #while 1:
        #x=g.next()
    while 1:
        x=g.next()
        y=g.next()
        if x!=y:
            count+=1
            index1=findPos(x)
            index2=findPos(y)
            index1,index2=min(index1,index2),max(index1,index)
            if x!=y:
                if y==PM:
                    x,y=y,x
                if not isInt(nums[y]):
                    nums[x]+=nums[y][:]
                    nums[y]=x
                    #if len(nums[x])>100000:
                        #print len(nums[x]), count
                    if x==PM or y==PM:
                        print x, y, time()-t
            if math.log(count,10).is_integer():
                print count
        if len(nums[PM])!=m:
            m=len(nums[PM])
            print m
        if len(nums[PM])>.99*10**l:
            print count, time()-t#, nums
            return
            

main(6)
    
