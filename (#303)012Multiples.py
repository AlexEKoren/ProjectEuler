import time
def main(a):
    t=time.time()
    nums=[]
    x=0
    count=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    count7=0
    count8=0
    count9=0
    count10=0
    count11=0
    count12=0
    count13=0
    count14=0
    count15=0
    count16=0
    count17=0
    count18=0
    while x<a:
        if count%3==0 or count%3==1:
            x+=1
        else:
            if count2%3==0 or count2%3==1:
                x+=8
            else:
                if count3%3==0 or count3%3==1:
                    x+=78
                else:
                    if count4%3==0 or count4%3==1:
                        x+=778
                    else:
                        if count5%3==0 or count5%3==1:
                            x+=7778
                        else:
                            if count6%3==0 or count6%3==1:
                                x+=77778
                            else:
                                if count7%3==0 or count7%3==1:
                                    x+=777778
                                else:
                                    if count8%3==0 or count8%3==1:
                                        x+=7777778
                                    else:
                                        if count9%3==0 or count9%3==1:
                                            x+=77777778
                                        else:
                                            if count10%3==0 or count10%3==1:
                                                x+=777777778
                                            else:
                                                if count11%3==0 or count11%3==1:
                                                    x+=7777777778
                                                else:
                                                    if count12%3==0 or count12%3==1:
                                                        x+=77777777778
                                                    else:
                                                        if count13%3==0 or count13%3==1:
                                                            x+=777777777778
                                                        else:
                                                            if count14%3==0 or count14%3==1:
                                                                x+=7777777777778
                                                            else:
                                                                if count15%3==0 or count15%3==1:
                                                                    x+=77777777777778
                                                                else:
                                                                    if count16%3==0 or count16%3==1:
                                                                        x+=777777777777778
                                                                    else:
                                                                        if count17%3==0 or count17%3==1:
                                                                            x+=7777777777777778
                                                                        else:
                                                                            if count18%3==0 or count18%3==1:
                                                                                x+=77777777777777778
                                                                            count18+=1
                                                                        count17+=1
                                                                    count16+=1
                                                                count15+=1
                                                            count14+=1
                                                        count13+=1
                                                    count12+=1
                                                count11+=1
                                            count10+=1   
                                        count9+=1
                                    count8+=1
                                count7+=1
                            count6+=1
                        count5+=1
                    count4+=1
                count3+=1
            count2+=1
        count+=1
        nums.append(x)
        if len(nums)>50000000:
            break
    print len(nums), nums[-2]
    total=0
    for x in range(1,100):
        if x%100==0:
            print x, time.time()-t
        temp=total
        for y in xrange(0,len(nums)):
            if nums[y]%x==0:
                total+=nums[y]/x
                if x==99 or x==9 or x==999:
                    print nums[y]
                break
        if temp==total:
            print x
    print total

                
main(10000000000000)
