def main(m):
    array=[m+1,2,4,7,11]
    r=11
    i=5
    while len(array)+2<2*m+1:
        array.append(r+i)
        r+=i
        i+=1
    while array[-1]<10**6:
        temp=0
        for y in range(1,len(array)-2*(m-3)*m+1):
            temp+=sum(array[:y])
        temp+=7
        array.append(temp)
    print array
    print array[-1], len(array)+1, array.count(7)
main(10)
