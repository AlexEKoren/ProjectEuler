import time
def nextGen(n):
    return n**2%50515093

def main(l):
    t=time.time()
    n=290797
    array=[n]
    total=0
    current=1
    for x in range(l):
        n=nextGen(n)
        array.append(n)
    print time.time()-t
    for i in range(1, len(array)):
        for j in range(i, len(array)):
            total+=min(array[i:j+1])
            #if array.index(min(array[i:j+1]))!=current and len(array)>2:
                #current=array.index(min(array[i:j+1]))
                #print current
    print total, time.time()-t
    
main(100)
    
