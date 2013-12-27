import time
import itertools
def main2(x):
    acceptables=[]
    y=0
    count=1
    sevens=1
    secondSevens=1
    thirdSevens=0
    sevensCounter=2
    while y<1000000:
        #print "1"
        if count%3==1:
            y+=1
            count+=1
            print y
        elif count%3==2:
            y+=1
            count+=1
            print y
        else:
            y+=8
            count+=1
            print y
        if count==9:
            count=1
            if sevens%3==1 or sevens%3==2:
                y+=78
                print y, "78"
            else:
                if secondSevens%3==1 or secondSevens%3==2:
                    y+=778
                    print y, "778"
                    secondSevens+=1
                else:
                    if thirdSevens%2==0:
                        sevensCounter+=1
                        thirdSevens=0
                    total=""
                    for x in range(sevensCounter):
                        total+="7"
                    total+="8"
                    print y, total
                    y+=int(total)
                    thirdSevens+=1
                    secondSevens+=1
            sevens+=1
        #print y
        acceptables.append(y)
    print acceptables, len(acceptables)

def main3(x):
    for y in range(1,x):
        temp=y
        count=0
        while str(y).__contains(3) or str(y).__contains(4) or str(y).__contains(5) or str(y).__contains(6) or str(y).__contains(7) or str(y).__contains(8) or str(y).__contains(9):
            if y%10==2:
                if count%2==0:
                    temp*=6
                else:
                    temp*=5
            #if y%10==3:

def main4():
    perms=[]
    total=2
    tried="111222222222222"
    for x in range(2,13):
        temp=list(itertools.product(range(3), repeat=x))
        for y in temp:
            tempStr=""
            for z in y:
                tempStr+=str(z)
            #print tempStr
            perms.append(int(tempStr))
        print x
    for x in range(14,20):
        perms2=list(itertools.combinations_with_replacement('120', x))
        for z in perms2:
            tempStr=""
            for y in z:
                tempStr+=str(y)
                #print tempStr
            perms.append(int(tempStr))
        print x
    for x in range(14,20):
        perms2=list(itertools.product('12', repeat=x))
        for z in perms2:
            tempStr=""
            for y in z:
                tempStr+=str(y)
            #print tempStr
            perms.append(int(tempStr))
        print x
    print len(perms)
    while perms.__contains__(0):
        perms.remove(0)
    perms.sort()
    print "started"
    for x in range(3,101):
        printed=False
        for y in perms:
            if y%x==0:
                if x%999==0:
                    print y, x, y/x, y%x
                if x==9899 or x==9989 or x==9999:
                    print y, x, y/x, y%x
                printed=True
                #print y, x, y/x, y%x
                total+=y/x
                break
        if printed==False:
            if 111222222222222%x==0:
                print "111222222222222", x, 111222222222222/x
                total+=111222222222222/x
            elif 1112222222222220%x==0:
                print "1112222222222220", x, 1112222222222220/x
                total+=1112222222222220/x
            elif 11112222222222222222%x==0:
                print "11112222222222222222", x, 11112222222222222222/x
                total+=11112222222222222222/x
            else:
                print "indivisible", x 
    print total
main2(100000000000)
#main4()
