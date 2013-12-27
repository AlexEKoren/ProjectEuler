def main(a):
    sq=[x**2 for x in range(a+1)]
    array=[0 for x in range(a+1)]
    for x in range(a):
        x2=x**2
        x6=6*x
        for i in range(int(x/6)+1,int(x/2)):
            temp=x6*i-x2-5*i**2
            if temp>=0 and temp<=a:
                array[temp]+=1
    print array.count(10)

main(10000)
