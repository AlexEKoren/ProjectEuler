from itertools import *
import random
import time
def createLists(x):
    perms=permutations(range(1,x+1),x)
    return perms

def createRandom(x):
    perms=permutations(range(x),3)
    return perms

def swap(swaps, array):
    temp=[array[swaps[0]],array[swaps[1]],array[swaps[2]]]
    random.shuffle(temp)
    array[swaps[0]]=temp[0]
    array[swaps[1]]=temp[1]
    array[swaps[2]]=temp[2]
    return array

def main(x):
    t=time.time()
    perms=list(createLists(x))
    swaps=list(createRandom(x))
    #print swaps
    finalPerms=list(perms[0])
    final=0
    for a in range(100):
        tCount=0
        for x in reversed(perms):
            temp=list(x)
            #print temp
            while temp!=finalPerms:
                #print temp, finalPerms
                temp=swap(random.choice(swaps),temp)
                tCount+=1
            #print tCount
        final+=tCount*1.0/len(perms)
    print final/100, time.time()-t
    return final/100
array=[]
for x in range(3,6):
    array.append(main(x))

for x in range(len(array)-1):
    print array[x+1]/array[x]
    
    
