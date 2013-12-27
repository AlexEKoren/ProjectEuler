import AEKsys
import time
size=0
def inArray(x,y):
    return x>=0 and y>=0 and x<size and y<size

def toString(a):
    s=""
    for x in a:
        temp=""
        for y in x:
            temp+="  "+str(y)+"  "
        s+=temp+"\n"
    return s

def main():
    global size
    f=(open(AEKsys.MyPrograms+"\\83.txt", "r")).readlines()
    mat=[]
    for y in f:
        #print y
        tempA=[]
        temp=""
        for x in y:
            #print x
            if x!="," and x!="\n":
                temp+=x
            else:
                #print temp
                tempA.append(int(temp))
                temp=""
        mat.append(tempA)
        tempA=[]
    #mat=[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
    size=len(mat)
    finalMat=mat[:]
    boolMat=[]
    for x in range(len(mat)):
        temp=[]
        for y in range(len(mat)):
            temp.append(False)
        boolMat.append(temp)
    boolMat[0][0]=True
    boolMat[0][1]=True
    boolMat[1][0]=True
    finalMat[0][1]=mat[0][0]+mat[0][1]
    finalMat[1][0]=mat[0][0]+mat[1][0]
    f=mat[-1][-1]
    while finalMat[-1][-1]==f:
        m=10**6
        mx=0
        my=0
        for x in range(len(mat)):
            for y in range(len(mat)):
                if boolMat[y][x]:
                    c=finalMat[y][x]
                    if inArray(x+1,y):
                        if boolMat[y][x+1]==False:
                            if c+mat[y][x+1]<m:
                                m=c+mat[y][x+1]
                                mx=x+1
                                my=y
                    if inArray(x-1,y):
                        if boolMat[y][x-1]==False:
                            if c+mat[y][x-1]<m:
                                m=c+mat[y][x-1]
                                mx=x-1
                                my=y
                    if inArray(x,y+1):
                        if boolMat[y+1][x]==False:
                            if c+mat[y+1][x]<m:
                                m=c+mat[y+1][x]
                                mx=x
                                my=y+1
                    if inArray(x,y-1):
                        if boolMat[y-1][x]==False:
                            if c+mat[y-1][x]<m:
                                m=c+mat[y-1][x]
                                mx=x
                                my=y-1
        finalMat[my][mx]=m
        boolMat[my][mx]=True
        #print toString(finalMat), boolMat
    print finalMat[-1][-1]
                                
                    
main()
                
                
        
