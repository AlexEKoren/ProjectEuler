def findPows(x):
    array=[]
    for y in range(2,x):
        for z in range(2,10):
            array.append(y**z)
    array.remove(4)
    array.remove(8)
    array.remove(9)
    array=list(set(array))
    array.sort()
    return array

def main(x):
    array=findPows(x)
    count=0
    for y in array:
        #print y
        total=0
        for z in str(y):
            total+=int(z)
        temp=total
        if total!=1:
            while total<y:
                total*=temp
        if total==y:
            count+=1
            print y, count
        if count==30:
            print y
            return
main(100)
