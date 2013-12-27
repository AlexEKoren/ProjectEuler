import itertools

def squares(x, y):
    s=[]
    z=x
    count=0
    while z<y:
        s.append(str(long(z**2))) 
        if count%2==0:
            z+=40
        else:
            z+=60
        count+=1
    return s
def main():
    a=1010101030
    print 1414213630>3162277660
    b=str(a**2)
    count=0
    while a<1389026623 and a>=1000000000:
        if b[2]=="2":
            if b[4]=="3":
                if b[6]=="4":
                    if b[8]=="5":
                        if b[10]=="6":
                            if b[12]=="7":
                                #print a
                                if b[14]=="8":
                                    if b[16]=="9":
                                        if b[18]=="0":
                                            break
        if count%2==1:
            a+=60
        elif count%2==0:
            a+=40
        b=str(a**2)
        count+=1
        print b[0], b[2], b[4], b[6], b[8], b[10], b[12], b[14], b[16], b[18], a
        #print b, a
    print a
def main2():
    s=squares(1000000030,1500000000)
    print "squares done"
    print len(s[-1])
    for x in s:
        if x[0]=="1":
            if x[2]=="2":
                if x[4]=="3":
                    if x[6]=="4":
                        if x[8]=="5":
                            if x[10]=="6":
                                if x[12]=="7":
                                    print x
                                    if x[14]=="8":
                                        if x[16]=="9":
                                            if x[18]=="0":
                                                print "final",x
                                                break
                                        

def main3():
    c=1020304050607080900
    x=10000000000000000010
    while int(((c+x)%10**19)**.5)!=((c+x)%10**19)**.5:
        if x%100000000==90909090:
            x+=909090910
        elif x%1000000==909090:
            x+=9090910
        elif x%10000==9090:
            #print "yes \n \n \n \n \n \n"
            x+=90910
        elif x%100==90:
            x+=910
        else:
            x+=10
        print (c+x)%10**19, x
    print c+x
main2()
