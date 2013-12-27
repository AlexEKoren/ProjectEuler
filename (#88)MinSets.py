from operator import mul
def mulArray(a):
    return reduce(mul,(x for x in a),1)
def findMin(k):
    array=[1]*(k-1)
    array.insert(-1,2)
    index=-1
    m=10**10
    final=[]
    while index!=int(.5*len(array))*-1:
        while sum(array)!=mulArray(array):
            array[index]+=1
            if array[index]>10**3:
                break
        if sum(array)<m:
            #print array, mulArray(array), sum(array)
            m=sum(array)
            final=array
        array[index]=2
        index-=1
        #print index
    return m

def main(a):
    s=[]
    for x in range(2,a+1):
        print x
        s.append(findMin(x))
    s=list(set(s))
    print sum(s)

main(12000)

