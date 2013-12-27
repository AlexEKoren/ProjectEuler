import random

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
    board=[]
    for x in range(40):
        board.append(0)
    pos=0
    count=0
    dub=0
    for x in range(a):
        r1=int(random.random()*4)+1
        r2=int(random.random()*4)+1
        #print r1+r2
        pos+=r1+r2
        if pos>39:
            pos-=40
        if r1==r2:
            dub+=1
        else:
            dub=0
        if pos==2 or pos==17 or pos==33:
            r=int(random.random()*16)
            if r==0:
                pos=0
            elif r==1:
                pos=10
        elif pos==7 or pos==2 or pos==36:
            r=int(random.random()*16)
            if r==0:
                pos=0
            if r==1:
                pos=10
            if r==2:
                pos=11
            if r==3:
                pos=24
            if r==4:
                pos=39
            if r==5:
                pos=5
            if r==7 or r==8:
                if pos==7:
                    pos=15
                if pos==22:
                    pos=25
                if pos==36:
                    pos=5
            if r==9:
                if pos==7 or pos==12:
                    pos=12
                if pos==22:
                    pos=28
            if r==10:
                pos-=3
        if pos==30 or dub==3:
            pos=10
            dub=0
        board[pos]+=1
    print board
    print findHighest3(board)

main(10**4)
