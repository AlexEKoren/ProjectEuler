def main():
    array=[]
    x=1
    while x<1000000:
        array.append(x)
        x=x+1
    m=0
    tempFinal=0
    final=0
    for i in reversed(array):
        temp2=i
        #print temp2
        while temp2>1:
            if temp2%2==1:
                temp2=temp2*3+1
                if temp2<1000000:
                    array[temp2]=0
            elif temp2%2==0:
                temp2=temp2/2
                if temp2<1000000:
                    array[temp2]=0
            m=m+1
        if m>tempFinal:
            tempFinal=m
            final=i
        m=0
    print final
main()
                
