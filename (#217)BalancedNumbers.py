def main(x):
    num=1
    mid=1
    total=0
    if 10**x>10000:
        while num<1000:
            if str(num)==str(num)[::-1]:
                total+=num
            num+=1
        while num<10**x:
            lAvg=0
            rAvg=0
            for y in range(len(str(num))/2):
                lAvg+=int(str(num)[y])
            if len(str(num))%2==1:
                for y in range(len(str(num))/2+1, len(str(num))):
                    rAvg+=int(str(num)[y])
            else:
                for y in range(len(str(num))/2, len(str(num))):
                    rAvg+=int(str(num)[y])
            #print lAvg, rAvg, num
            if lAvg==rAvg:
                total+=num
                #print num
            num+=1
    else:
        while num<10**x:
            if str(num)==str(num)[::-1]:
                total+=num
            num+=1
    
    print total%(3**15)
main(7)
