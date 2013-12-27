import itertools
def binToDec(x):
    power=0
    total=0
    for y in reversed(x):
        total+=int(y)*(2**power)
        power+=1
    return total
def main(x):
    array=[]
    total=0
    perms=list(itertools.product('10', repeat=2**x))
    perms.sort()
    print len(perms)
    for y in perms:
        array.append(y)
    array=[]
    for y in reversed(perms):
        a=y
        double=False
        count=0
        while count<2**x-1:
            a=str(a)[1:]+str(a)[0]
            if perms.__contains__(a):
                double=True
                break
            count+=1
        if double==True:
            perms.remove(y)
    print len(perms)
    for y in perms:
        temp=[]
        z=0
        while z<len(y)-2:
            temp.append(y[z]+y[z+1]+y[z+2])
            z+=1
        temp.append(y[-2]+y[-1]+y[0])
        temp.append(y[-1]+y[0]+y[1])
        if len(temp)==len(list(set(temp))):
            print temp
            array.append(temp)
        
    print total
    return total

main(3)
