import random
def tris(x):
    tris=[]
    for n in range(x):
        tris.append(n*(n+1)/2)
    return tris

def squares(x):
    squares=[]
    for n in range(x):
        squares.append(n**2)
    return squares

def pents(x):
    pents=[]
    for n in range(x):
        pents.append(n*(3*n-1)/2)
    return pents

def hexagonals(x):
    hexs=[]
    for n in range(x):
        hexs.append(n*(2*n-1))
    return hexs

def hepts(x):
    hepts=[]
    for n in range(x):
        hepts.append(n*(5*n-3)/2)
    return hepts

def octs(x):
    octs=[]
    for n in range(x):
        octs.append(n*(3*n-2))
    return octs

def findAll(x):
    tris=[]
    squares=[]
    pents=[]
    hexs=[]
    hepts=[]
    octs=[]
    for n in range(1,x):
        increment=(n-1)*((n-1)+1)/2
        base=n*(n+1)/2
        tris.append(base)
        squares.append(base+increment)
        pents.append(base+increment*2)
        hexs.append(base+increment*3)
        hepts.append(base+increment*4)
        octs.append(base+increment*5)
    return tris, squares, pents, hexs, hepts, octs

def main(x,b):
    array=findAll(x)
    #print array
    tris=array[0]
    squares=array[1]
    pents=array[2]
    hexs=array[3]
    hepts=array[4]
    octs=array[5]
    print "done"
    while 1==1:
        for n in range(1001,10000):
            #print n
            array=[n]
            count=1
            temp=n
            triDone,squareDone,pentDone,hexDone,heptDone,octDone=False,False,False,False,False,False
            if tris.__contains__(n):
                triDone=True
                #print "tri"
            elif squares.__contains__(n):
                squareDone=True
                #print "square"
            elif pents.__contains__(n):
                pentDone=True
                #print "pent"
            elif hexs.__contains__(n):
                hexDone=True
                #print "hex"
            elif hepts.__contains__(n):
                heptDone=True
                #print "hept"
            elif octs.__contains__(n):
                octDone=True
                #print "oct"
            else:
                continue
            if temp%100/10==0:
                continue
            p=0
            cont=True
            total=n
            #print n
            last2=temp/100
            temp=temp%100*100+b
            lim=temp+100-b
            while temp<lim:
                change=False
                #print temp
                if tris.__contains__(temp) and temp%100/10!=0:
                    if triDone==False:
                        triDone=True
                        change=True
                if squares.__contains__(temp) and temp%100/10!=0:
                    if squareDone==False:
                        squareDone=True
                        change=True
                if pents.__contains__(temp) and temp%100/10!=0:
                    if pentDone==False:
                        pentDone=True
                        change=True
                if hexs.__contains__(temp) and temp%100/10!=0:
                    if hexDone==False:
                        hexDone=True
                        change=True
                if hepts.__contains__(temp) and temp%100/10!=0:
                    if heptDone==False:
                        heptDone=True
                        change=True
                if octs.__contains__(temp) and temp%100/10!=0:
                    if octDone==False:
                        octDone=True
                        change=True
                if change==True:
                    total+=temp
                    array.append(temp)
                    r=int(random.random()*100)
                    temp=temp%100*100+r
                    lim=temp+100-r
                    count+=1
                if count!=6:
                    temp+=1
                if count==6:
                    print array
                    if temp/100==last2:
                        print last2, temp/100
                        print array
                        print total
                        return
                    else:
                        break
            #print array
main(200, 0)
