import time
import math
def makeSqs(a):
    return [x**2 for x in range(a)]

def main(a,l):
    t=time.time()
    sq=makeSqs(a)
    nums=[0 for x in range(l+1)]
    s=int(math.sqrt(l))
    '''for x in range(4,a):
        for i in range(int(x/2),int(x/5),-1):
            temp=sq[x]-sq[x-i]-sq[x-i*2]
            if temp>l:
                #print x, i
                continue
            if temp<0:
                print x, i
                break
            #print x, i, temp
            nums[temp]+=1'''
    for i in range(1,int(a/5)+10):
        #print i
        r=6*i
        q=5*sq[i]
        for x in range(2*i+1,min(a,5*i)):
            #print x
            temp=x*r-sq[x]-q
            if temp<0:
                #print x, i, temp
                break
            if temp>l:
                #print x, i, temp
                continue
            nums[temp]+=1
    print nums.index(10)
    n=[x for x in range(len(nums)) if nums[x]==10]
    print n[:30]
    print nums.count(10),time.time()-t

main(100000,10**6)
