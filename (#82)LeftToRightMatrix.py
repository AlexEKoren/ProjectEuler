import AEKsys
import time
def main():
    f=(open(AEKsys.MyPrograms+"\\82.txt", "r")).readlines()
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
    t=time.time()
    finalMat=mat[:]
    x=len(mat)-1
    while x>0:
        y=0
        while y<len(mat):
            if y==0:
                finalMat[y][x-1]+=min(finalMat[y][x],finalMat[y+1][x]+mat[y+1][x-1],finalMat[y+1][x]+mat[y][x],
                                      mat[y+1][x-1]+mat[y+2][x-1]+finalMat[y+2][x])
            elif y>=len(mat)-2:
                finalMat[y][x-1]+=min(finalMat[y][x],finalMat[y-1][x-1],finalMat[y-1][x]+mat[y][x])
            else:
                finalMat[y][x-1]+=min(finalMat[y][x],finalMat[y-1][x-1],finalMat[y+1][x]+mat[y+1][x-1],
                                      finalMat[y+1][x]+mat[y][x],finalMat[y-1][x]+mat[y][x],
                                      mat[y+1][x-1]+mat[y+2][x-1]+finalMat[y+2][x])
            y+=1
        x-=1
    print min(finalMat[y][0] for y in range(len(finalMat))), time.time()-t
    
                    
main()
