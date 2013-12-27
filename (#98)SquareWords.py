import AEKsys
from itertools import *
def squares(x):
    s=[]
    y=10
    while y**2<x:
        s.append(str(y**2))
        y+=1
    return s

def main():
    f=(open(AEKsys.MyPrograms+ "\\words.txt","r")).readlines()
    words=[]
    temp=""
    for x in f[0]:
        if x==",":
            continue
        if x=="\"":
            temp+=x
            if temp.count("\"")==2:
                words.append([temp[1:-1], len(temp)-2])
                temp=""
        else:
            temp+=x
    doubles=[]
    for x in range(len(words)-1):
        for y in range(x+1, len(words)):
            if words[x][1]==words[y][1]:
                a=list(words[x][0])
                a.sort()
                b=list(words[y][0])
                b.sort()
                if a==b:
                    doubles.append([words[x][0],words[y][0]])
                    #print words[x][0], words[y][0]
    print doubles
    sq=squares(10**7)
    dubSq=[]
    for x in range(len(sq)-1):
        for y in range(x+1, len(sq)):
            if len(sq[x])==len(sq[y]):
                a=list(sq[x])
                a.sort()
                b=list(sq[y])
                b.sort()
                if a==b:
                    dubSq.append([sq[x],sq[y]])
                    #print sq[x],sq[y]
    print len(dubSq)
    m=0
    m=1
    for x in doubles:
        order=""
        for z in x[0]:
            order+=str(x[1].index(z))
        #print order, x
        for y in dubSq:
            if len(y[0])>len(x[0]):
                break
            order2=""
            for z in y[0]:
                order2+=str(y[1].index(z))
            #print order2
            if order==order2:
                #print order, order2
                if int(y[0])>int(y[1]):
                    if y[0]>m:
                        print m
                        m=int(y[0])
                        print "m=",m
                else:
                    if y[1]>m:
                        m=int(y[1])
                        print "m=",m
                break

main()
