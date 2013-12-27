import itertools
import time
t=time.time()
def main(z):
    array=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for p in range(0, z+1):
        count=0
        for x in list(itertools.product('AOL',repeat=p)):
            b=False
            lcount=0
            for y in x:
                if y=='L':
                    lcount+=1
                if lcount>1:
                    b=True
                    break
            if b==False:
                s=""
                for y in x:
                    s+=y
                if not s.__contains__('AAA'):
                    count+=1
        array.append(count)
    return array

def main2(b,a):
    t=time.time()
    array=b
    for x in range(len(array)-1, a):
        temp=array[x-1]
        y=x-2
        while y>16:
            temp-=array[y]
            y-=1
        temp=array[x]*2+temp
        c=5
        while c<len(array):
            temp-=array[x-c]
            c+=3
        array.append(temp)
    print array

main2(main(2), 46)
print time.time()-t
