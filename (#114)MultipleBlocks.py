def main(m,n):
    array=[4,2,4,7,11,17]
    for x in range(6,n-1):
        temp=0
        for y in range(1,len(array)-m+1):
            temp+=sum(array[:y])
        temp+=7
        array.append(temp)
    print array[-1]
main(3,50)
