import AEKsys
import time
def checkRow(array, a, y):
    row=array[y]
    for x in row:
        if x==a:
            return False
    return True

def checkCol(array, a, x):
    y=0
    while y<len(array):
        #print x, y, len(array)
        if array[y][x]==a:
            return False
        y+=1
    return True

def notInSquare(array, a, x, y):
    for b in range(y-y%3, y+3-y%3):
        for c in range(x-x%3, x+3-x%3):
            #print b, c, len(array), len(array[b])
            if array[b][c]==a:
                return False
    return True

def onlyInSquare(array, a, x, y):
    if notInSquare(array, a, x, y):
        only=True
        pos=[]
        for b in range(y-y%3, y+3-y%3):
            for c in range(x-x%3, x+3-x%3):
                if array[b][c]=="0":
                    if checkRow(array, a, b):
                        if checkCol(array, a, c):
                            pos.append([b,c])
        #print pos, x, y, a
        return pos
    return []

def finishRow(array, a, y):
    pos=[]
    if checkRow(array, a, y):
        for x in range(len(array[y])):
            if array[y][x]=="0":
                if checkCol(array, a, x) and notInSquare(array, a, x, y):
                    pos.append([y, x])
        return pos
    return []

def finishCol(array, a, x):
    pos=[]
    if checkCol(array, a, x):
        for y in range(len(array)):
            if array[y][x]=="0":
                if checkRow(array, a, y) and notInSquare(array, a, x, y):
                    pos.append([y, x])
        return pos
    return [] 

def checkVertHor(array, a, x, y):
    for b in range(y-y%3, y+3-y%3):
        if b!=y:
            if checkCol(array, a, y):
                return False
            for c in range(x-x%3, x+3-x%3):
                if c!=x:
                    if checkRow(array, a, y):
                        return False
    return True

def toString(a):
    final=""
    for x in a:
        temp=""
        for y in x:
            temp+=y+" "
        final+=temp+"\n"
    return final

def main():
    f=(open(AEKsys.MyPrograms+"\\sudoku.txt","r")).readlines()
    count=0
    temp=[]
    puzzles=[]
    for x in f:
        if count%10==0 and count!=0:
            puzzles.append(temp)
            #print temp
            temp=[]
        count+=1
        if len(x)>9:
            temp.append(list(x[0:9]))
    nums=[]
    for x in range(1,10):
        nums.append(str(x))
    total=0
    p=0
    t=time.time()
    while p<len(puzzles):
        a=puzzles[p]
        print toString(a)
        all3=False
        total+=runChecks(a, nums)
        p+=1
    print total

def runChecks(a, nums):
        t=time.time()
        all3=False
        total=0
        while a[0][0]=="0" or a[0][1]=="0" or a[0][2]=="0" and time.time()-t<4:
            if 1:
                for y in range(len(a)):
                    for x in range(len(a[y])):
                        #print y, x
                        if a[y][x]=="0":
                            for n in nums:
                                oS=onlyInSquare(a, n, x, y)
                                #print o
                                if len(oS)==1:
                                    a[oS[0][0]][oS[0][1]]=n
                                    #print toString(a)
                                    t=time.time()
                                if checkVertHor(a, n, x, y):
                                    if checkRow(a, n, y):
                                        if checkCol(a, n, y):
                                            if notInSquare(a, n, x, y):
                                                #print x, y
                                                #print toString(a)
                                                t=time.time()
                                                a[y][x]=n
                                fR=finishRow(a, n, y)
                                #print fR, x, y
                                if len(fR)==1:
                                    a[fR[0][0]][fR[0][1]]=n
                                if a[0][0]!="0" and a[0][1]!="0" and a[0][2]!="0":
                                    all3=True
                                    break
                            #print x, y
                            if all3==True:
                                break
                    if all3==True:
                        break
                for y in range(len(a)):
                    for x in range(len(a[y])):
                        if a[y][x]=="0":
                            #print x, y
                            temp=[]
                            for n in nums:
                                temp.append(n)
                            for n in nums:
                                if checkRow(a, n, y)==False or checkCol(a, n, x)==False or notInSquare(a, n, x, y)==False:
                                    temp.remove(n)
                            #print temp
                            if len(temp)==1:
                                a[y][x]=temp[0]
                                #print toString(a)
                            else:
                                a[y][x]="0"
                for y in range(len(a)):
                    temp=[]
                    for n in nums:
                        temp.append(n)
                    for x in range(len(a[y])):
                        if a[y][x]!="0":
                            #print temp, a[y][x]
                            temp.remove(a[y][x])
                    for x in range(len(a[y])):
                        temp2=[]
                        for n in temp:
                            temp2.append(n)
                        #print y, temp2
                        if a[y][x]=="0":
                            for n in temp2:
                                if checkCol(a, n, x)==False:
                                    temp2.remove(n)
                        if len(temp2)==1:
                            if checkCol(a, temp2[0], x):
                                a[y][x]=temp2[0]
                                temp.remove(temp2[0])
                for x in range(len(a)):
                    temp=[]
                    for n in nums:
                        temp.append(n)
                    for y in range(len(a[y])):
                        if a[y][x]!="0":
                            #print temp, a[y][x]
                            #print toString(a)
                            temp.remove(a[y][x])
                    for y in range(len(a[y])):
                        temp2=[]
                        for n in temp:
                            temp2.append(n)
                        #print x, temp2
                        if a[y][x]=="0":
                            for n in temp2:
                                if checkRow(a, n, y)==False:
                                    temp2.remove(n)
                        if len(temp2)==1:
                            if checkRow(a, temp2[0], y):
                                a[y][x]=temp2[0]
                                temp.remove(temp2[0])
                t=time.time()
                print toString(a)
                                       
        total+=int(a[0][0]+a[0][1]+a[0][2])
        print total
        print toString(a)
        return total
    
main()

    
