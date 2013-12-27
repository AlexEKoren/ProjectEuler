import random

pos=0

def rollDice(x):
    r1=int(random.random()*x)+1
    r2=int(random.random()*x)+1
    if r1==r2:
        return r1+r2, True
    return r1+r2, False

def nextR():
    global pos
    while pos%5!=0 or pos%10==0:
        pos+=1
        if pos>=40:
            pos=0
    return pos

def nextU():
    global pos
    while pos!=12 and pos!=28:
        pos+=1
        if pos>=40:
            pos=0
    return pos

def rPos():
    global pos
    return pos

def shiftCards(l):
    temp=l[0]
    for x in range(1,15):
        l[x-1]=l[x]
        l[15]=temp
    return l

def findHighest3(l):
    m1=0
    for x in l:
        if x>m1:
            m1=x
    m2=0
    for x in l:
        if x>m2 and x!=m1:
            m2=x
    m3=0
    for x in l:
        if x>m3 and x!=m1 and x!=m2:
            m3=x
    return l.index(m1),l.index(m2),l.index(m3)

def main(a):
    global pos
    CHC=[0,11,24,39,5,"1","1","2","3",10]
    for x in range(6):
        CHC.append("4")
    COC=[0,10]
    for x in range(14):
        COC.append("4")
    random.shuffle(CHC)
    #print CHC
    random.shuffle(COC)
    board=[]
    for x in range(40):
        board.append(0)
    count=0
    for x in range(a):
        #print pos
        temp=rollDice(6)
        if temp[1]==True:
            count+=1
        else:
            count=0
        #print pos
        pos+=temp[0]        
        if count==3:
            count=0
            pos=10
        if pos==2 or pos==17 or pos==33:
            temp1=COC[0]
            if temp1=="4":
                pos=rPos()
            else:
                pos=COC[0]
            COC=shiftCards(COC)
        elif pos==7 or pos==22 or pos==36:
            temp1=CHC[0]
            if temp1=="1":
                pos=nextR()
                #print "yes"
            elif temp1=="2":
                pos=nextU()
            elif temp1=="4":
                pos=rPos()
            elif temp1=="3":
                pos-=3
            else:
                pos=CHC[0]
            CHC=shiftCards(CHC)
        elif pos==30:
            pos=10
        if pos>=40:
            pos=pos%40
        board[pos]+=1
    return findHighest3(board)


def main2(a):
    final=[]
    for x in range(40):
        final.append([0,0,0])
    for x in range(a):
        temp=main(10**4)
        final[temp[0]][0]+=1
        final[temp[1]][1]+=1
        final[temp[2]][2]+=1
    m1=0
    m1A=0
    for x in final:
        if x[0]>m1:
            m1=x[0]
            m1A=final.index(x)
    m2=0
    m2A=0
    for x in final:
        if x[1]>m2 and x[1]!=final[m1A][1]:
            m2=x[1]
            m2A=final.index(x)
    m3=0
    m3A=0
    for x in final:
        if x[2]>m3  and x[2]!=final[m1A][1]  and x[2]!=final[m2A][2]:
            m3=x[2]
            m3A=final.index(x)
    print m1A,m2A,m3A

for x in range(15):          
    main2(10**2)
