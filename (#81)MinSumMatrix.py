import AEKsys
def main():
    f=(open(AEKsys.MyPrograms+"\\#81matrix.txt", "r")).readlines()
    #print f
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
    '''for x in mat:
        for y in x:
            if y/100==0:
                print mat.index(x), x.index(y), y'''
    print mat[0]
    x=1
    #while x<80:
        #mat[0][x]=mat[0][x-1]+mat[0][x]
        #mat[x][0]=mat[x-1][0]+mat[x][0]
        #x+=1
    print mat[-1]
    #mat=[[131,674,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
    x=1
    while x<len(mat):
        mat[0][x]=mat[0][x-1]+mat[0][x]
        mat[x][0]=mat[x-1][0]+mat[x][0]
        x+=1
    cx=1
    cy=1
    while 1:
        #print cx
        if cx==len(mat) and cy!=len(mat)-1:
            cx=0
            cy+=1
        elif cx==len(mat) and cy==len(mat)-1:
            print mat[-1][-1]
            break
        elif mat[cy-1][cx]<mat[cy][cx-1]:
            mat[cy][cx]=mat[cy-1][cx]+mat[cy][cx]
            #print mat[cy][cx]
        elif mat[cy][cx-1]<mat[cy-1][cx]:
            mat[cy][cx]=mat[cy][cx-1]+mat[cy][cx]
        cx+=1
        #print mat
        #print "\n"

        
    print mat[-1][-1]
    print mat[-2],mat[-1]
    
        
main()

