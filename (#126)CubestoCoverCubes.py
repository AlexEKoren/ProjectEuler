def main():
    array=[]
    for x in range(5000):
        array.append(0)
    for x in range(1,500):
        for y in range(x,500):
            for z in range(y,500):
                temp=x*y*2+x*z*2+y*z*2
                temp2=24
                while temp<1000:
                    array[temp]+=1
                    temp+=temp2
                    temp2+=8
    for x in array:
        if x>=10:
            print array.index(x)
            break
    #print array
main()
