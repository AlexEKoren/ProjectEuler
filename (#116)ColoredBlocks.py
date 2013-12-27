def main(n):
    total=0
    twos=[0]
    fibs1=0
    fibs2=1
    fibs=[1]
    for x in range(n):
        temp=fibs1+fibs2
        fibs.append(temp)
        fibs1=fibs2
        fibs2=temp
    for x in fibs:
        twos.append(twos[-1]+x)
    total+=twos[n-1]
    threes=[0,0,1,2,3,5]
    for x in range(6,n):
        threes.append(threes[x-3]+1+threes[x-1])
    total+=threes[-1]
    fours=[0,0,0,1,2,3,4,6]
    for x in range(8,n):
        fours.append(fours[x-4]+1+fours[x-1])
    total+=fours[-1]
    print total

def number117(n):
    array=[1,1,2,4,8,15,29]
    for x in range(6,n):
        temp=1
        temp+=sum(array[:-1])
        temp+=sum(array[:-2])
        temp+=sum(array[:-3])
        array.append(temp)
    print array[-1]
    
#main(50)
number117(50)

