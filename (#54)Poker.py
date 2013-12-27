import AEKsys
def BSort(cards):
    swapped=True
    while swapped==True:
        swapped=False
        for y in range(0, len(cards)-1):
            if int(cards[y][0])>int(cards[y+1][0]):
                temp=cards[y]
                cards[y]=cards[y+1]
                cards[y+1]=temp
                swapped=True
    return cards

def checkFoaK(a):
    if a[0][0]==a[1][0] and a[0][0]==a[2][0] and a[0][0]==a[3][0]:
        return True
    elif a[1][0]==a[2][0] and a[1][0]==a[3][0] and a[1][0]==a[4][0]:
        return True
    return False

def checkFullHouse(a):
    if a[0][0]==a[1][0] and a[0][0]==a[2][0]:
        if a[3][0]==a[4][0]:
            return True
    elif a[2][0]==a[3][0] and a[2][0]==a[4][0]:
        if a[0][0]==a[1][0]:
            return True
    return False

def checkToaK(a):
    if a[0][0]==a[1][0] and a[0][0]==a[2][0]:
        return True
    elif a[1][0]==a[2][0] and a[1][0]==a[3][0]:
        return True
    elif a[2][0]==a[3][0] and a[2][0]==a[4][0]:
        return True
    if len(a)>5:
        if a[3][0]==a[4][0] and a[3][0]==a[5][0]:
            return True
        if len(a)>6:
            if a[5][0]==a[4][0] and a[5][0]==a[6][0]:
                return True
    return False

def checkDoublePair(a):
    if a[0][0]==a[1][0] and a[2][0]==a[3][0]:
        if a[0][0]=="1":
            return 16.14
        else:
            return 16+int(a[2][0])/100.0
    elif a[1][0]==a[2][0] and a[3][0]==a[4][0]:
        if a[1][0]=="1":
            return 16.14
        else:
            return 16+int(a[4][0])/100.0
    elif a[0][0]==a[1][0] and a[3][0]==a[4][0]:
        if a[0][0]=="1":
            return 16.14
        else:
            return 16+int(a[3][0])/100.0
    return False

def checkPair(a):
    if a[0][0]==a[1][0]:
        return 15+int(a[0][0])/100.0
    elif a[1][0]==a[2][0]:
        return 15+int(a[1][0])/100.0
    elif a[2][0]==a[3][0]:
        #print 15+int(a[0][0])/100.0, a[0][0]
        return 15+int(a[2][0])/100.0
    elif a[3][0]==a[4][0]:
        if a[3][0]=="1":
            return 15.14
        else:
            return 15+int(a[3][0])/100.0
    return False

def checkStraight(a):
    x=0
    while x<4:
        if int(a[x][0])!=(int(a[x+1][0])-1):
            return False
        x+=1
    if len(a)>5:
        x=1
        while x<6:
            if int(a[x][0])!=(int(a[x+1][0])-1):
                return False
            x+=1
    return True

def checkFlush(a):
    x=0
    while x<4:
        if a[x][1]!=a[x+1][1]:
            return False
        x+=1
    return True


def main():
    f=(open(AEKsys.MyPrograms+ "\\poker.txt","r")).readlines()
    #print f
    cards=[]
    count=0
    count2=0
    for l in f:
        cards.append(l.split('\n'))
    for l in cards:
        l[0]=l[0].split(" ")
    #print cards[0][0][0]
    for x in cards:
        #print x
        p1S=0
        p2S=0
        p1=[]
        p2=[]
        for l in range(5):
            if x[0][l][0]=='T':
                #print "10"
                p1.append([10,x[0][l][1]])
            elif x[0][l][0]=='J':
                #print "J"
                p1.append([11,x[0][l][1]])
            elif x[0][l][0]=='Q':
                #print "Q"
                p1.append([12,x[0][l][1]])
            elif x[0][l][0]=='K':
                #print "K"
                p1.append([13,x[0][l][1]])
            elif x[0][l][0]=='A':
                #print "A"
                p1.append([14,x[0][l][1]])
                #p1.append([1,x[0][l][1]])
            else:
                p1.append([x[0][l][0],x[0][l][1]])
        for l in range(5,10):
            if x[0][l][0]=='T':
                #print "10"
                p2.append([10,x[0][l][1]])
            elif x[0][l][0]=='J':
                #print "J"
                p2.append([11,x[0][l][1]])
            elif x[0][l][0]=='Q':
                #print "Q"
                p2.append([12,x[0][l][1]])
            elif x[0][l][0]=='K':
                #print "K"
                p2.append([13,x[0][l][1]])
            elif x[0][l][0]=='A':
                #print "A"
                p2.append([14,x[0][l][1]])
                #p2.append([1, x[0][l][1]])
            else:
                p2.append([x[0][l][0],x[0][l][1]])
        #print p1
        p1=BSort(p1)
        #print p1
        p2=BSort(p2)
        if checkStraight(p1)==True and checkFlush(p1)==True:
            p1Score=22
            #print p1
        if checkFoaK(p1)==True:
            p1Score=21
            #print p1
        elif checkFullHouse(p1)==True:
            p1Score=20
            #print p1
        elif checkFlush(p1)==True:
            p1Score=19
            #print p1
        elif checkStraight(p1)==True:
            p1Score=18
            #print p1
        elif checkToaK(p1)==True:
            p1Score=17
            #print p1
        elif checkDoublePair(p1)!=False:
            p1Score=checkDoublePair(p1)
            #print p1
        elif checkPair(p1)!=False:
            p1Score=checkPair(p1)
        else:
            p1Score=int(p1[-1][0])
        if checkStraight(p2)==True and checkFlush(p2)==True:
            p2Score=22
            #print p2
        if checkFoaK(p2)==True:
            p2Score=21
            #print p2
        elif checkFullHouse(p2)==True:
            p2Score=20
            #print p2
        elif checkFlush(p2)==True:
            p2Score=19
            #print p2
        elif checkStraight(p2)==True:
            p2Score=18
            #print p2
        elif checkToaK(p2)==True:
            p2Score=17
            #print p2
        elif checkDoublePair(p2)!=False:
            p2Score=checkDoublePair(p2)
            #print p2, p2Score
        elif checkPair(p2)!=False:
            p2Score=checkPair(p2)
        else:
            p2Score=int(p2[-1][0])
        if p1Score>p2Score:
            count+=1
            #print p1, p1Score
            #print p2, p2Score, "\n"
        elif p1Score==p2Score:
            print p1
            print p2
            print
        else:
            count2+=1
        
    print count, count2


            
main()
