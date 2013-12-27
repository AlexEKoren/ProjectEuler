import time
from graphics import *
def changeString(x):
    temp=""
    for y in x:
        if y=="a":
            temp+="aRbFR"
        elif y=="b":
            temp+="LFaLb"
        else:
            temp+=y
    return temp

def XoR(s):
    temp=""
    for x in s:
        if x=="L":
            temp+="R"
        else:
            temp+="L"
    return temp

def makeString(x):
    count=0
    temp="RR"
    while count<x:
        temp=temp+"R"+XoR(temp[::-1])
        count+=1
    temp+="R"
    a=0
    i=4
    while a<len(temp):
        temp=temp[0:a]+"a"+temp[a:]
        temp=temp[0:a+2]+"b"+temp[a+2:]
        a+=i
        
    a=0
    i=4
    while a<len(temp):
        temp=temp[0:a]+"F"+temp[a:]
        a+=i
    return temp

def main(a, c):
    win=GraphWin("Heighway Dragon", 600,600)
    win.setCoords(c*-1*10/3,c*-1*2,c,c*2)
    t=time.time()
    '''s1="FaRbFRRL"
    s2="FaLbFRRL"
    end="FR"
    temp=""
    for x in range(2**(a-2)):
            temp+=s1+s2
    temp=temp[0:-4]
    temp+=end'''
    s="Fa"
    '''for l in range(a):
        s=changeString(s)'''
    s=makeString(a)
    #print s
    d=[0,1]
    x=0
    y=0
    count=0
    count2=0
    print time.time()-t
    temp=""
    '''for z in s:
        #print count
        temp+=z
        #print temp
        if temp=="FaRbFRRL":
            if count%8==7:
                count2+=1
                if count2%8==0:
                    print 1,
            temp=""
        elif temp=="FaLbFRRL":
            if count%8==7:
                count2+=1
                if count2%8==0:
                    print 2,
            temp=""
        elif temp=="FaRbFRLL":
            if count%8==7:
                count2+=1
                if count2%8==0:
                    print 3,
            temp=""
        elif temp=="FaLbFRLL":
            if count%8==7:
                count2+=1
                if count2%8==0:
                    print 4,
            temp=""
        if temp=="":
            count+=1'''
    count=0
    count2=0
    for z in s:
        '''if z=="F":
            print count2'''
        #print count
        #if count==10 or count==100 or count==1000 or count==10000 or count==100000 or count==1000000 or count==10**7:
        #print a, count, x, y
        if x==18 and y==16:
            print count
        '''if y==0 and z=="F":
            print "y=0", count
        if x==-3 and y==-2 and z=="F":
            print count'''
        '''if x==y and z=="F":
            print count, x, y'''
        if z=="F":
            x+=d[0]
            y+=d[1]
            count+=1
        elif z=="R":
            d=[d[1], d[0]*-1]
        elif z=="L":
            d=[d[1]*-1,d[0]]
        #print x, y, z, d
        Point(x,y).draw(win)
        count2+=1
    print x, y, count
    #print s, len(s)/8, time.time()-t
print XoR("R")
main(15,50)
