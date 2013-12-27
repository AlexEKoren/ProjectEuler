import time
def findBouncies():
    bouncy=[]
    for x in range(100,1000):
        s=str(x)
        if (s[0]>=s[1] and s[1]>s[2]) or (s[0]>s[1] and s[1]>=s[2]):
            p=1
        elif (s[0]<=s[1] and s[1]<s[2]) or (s[0]<s[1] and s[1]<=s[2]):
            p=1
        elif s[0]==s[1] and s[1]==s[2]:
            p=1
        else:
            bouncy.append(str(x))
    return bouncy

def findUps():
    ups=[]
    for x in range(10,100):
        if str(x)[0]<str(x)[1]:
            ups.append(str(x))
    return ups
def findDowns():
    ups=[]
    for x in range(10,100):
        if str(x)[0]>str(x)[1]:
            ups.append(str(x))
    return ups

def collapse(x):
    s=str(x)
    a=0
    f=""
    while a<len(s)-1:
        while s[a]==s[a+1]:
            a+=1
            if a==len(s)-1:
                break
        f+=s[a]
        a+=1
    if s[-1]!=f[-1]:
        f+=s[-1]
    return f
        
def main(x):
    t=time.time()
    #ups=findUps()
    #downs=findDowns()
    bouncies=findBouncies()
    #print bouncies
    total=99
    totalBouncies=0
    y=100
    while 1==1:
        total+=1
        #print y, collapse(y)
        #print y, totalBouncies*1.0/total
        a=collapse(y)
        for z in bouncies:
            #print z, collapse(y), y
            if a.__contains__(z):
                #print "yep"
                #print a, z
                totalBouncies+=1
                break
        '''for z in ups:
            a=collapse(y)
            if a.__contains__(z):
                for b in downs:
                    if a.__contains__(b):
                        totalBouncies+1
                        '''
        if totalBouncies*1.0/total>=x/100.0:
            print time.time()-t
            print y, totalBouncies*1.0/total
            return
        y+=1
    
    
#main(99)

def isBouncy(x):
    up=False
    down=False
    while x>0:
        if x/10==0:
            break
        
        if x%10>x/10%10:
            up=True
        if x%10<x/10%10:
            down=True
        if up and down:
            return True
        x/=10
    return False

def main2(a):
    count=0
    total=100
    x=101
    while count*1.0/total<a:
        if isBouncy(x):
            #print x
            count+=1
        total+=1
        x+=1
    print x
main2(.99)



    
#print collapse(111222333)
#print len(findBouncies())
        
            
