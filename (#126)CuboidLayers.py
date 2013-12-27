def copyCube(cube,x,y,z):
    new = []
    for a in range(x):
        t=[]
        for b in range(y):
            r=[]
            for c in range(z):
                r.append(cube[a][b][c])
            t.append(r)
        new.append(t)
    return new

def buildCube(x,y,z):
    cube=[]
    sx=x+26
    sy=y+26
    sz=z+26
    for a in range(sx):
        t=[]
        for b in range(sy):
            r=[]
            for c in range(sz):
                r.append(False)
            t.append(r)
        cube.append(t)
    startX=sx/2-x/2
    startY=sy/2-y/2
    startZ=sz/2-z/2
    for a in range(startX,startX+x):
        for b in range(startY,startY+y):
            for c in range(startZ,startZ+z):
                cube[a][b][c]=True
    counts=[]
    for repeat in range(13):
        newCube = copyCube(cube,sx,sy,sz)
        for a in range(startX-repeat,startX+x+repeat):
            for b in range(startY-repeat,startY+y+repeat):
                for c in range(startZ-repeat,startZ+z+repeat):
                    if cube[a][b][c]:
                        #print a,b,c
                        newCube[a+1][b][c]=True
                        newCube[a-1][b][c]=True
                        newCube[a][b+1][c]=True
                        newCube[a][b-1][c]=True
                        newCube[a][b][c+1]=True
                        newCube[a][b][c-1]=True
        count=0
        for a in range(sx):
            for b in range(sy):
                for c in range(sz):
                    if newCube[a][b][c] and not cube[a][b][c]:
                        count+=1
        counts.append(count)
        cube=copyCube(newCube,sx,sy,sz)
    return counts

def main():
    counts=[0]*(10**6+1)
    for x in range(1,20):
        for y in range(x,20):
            for z in range(y,20):
                c=buildCube(x,y,z)
                print x, y, z, c
                for a in c:
                    counts[a]+=1
                    if a==154:
                        print "YAY"
                    if counts[a]>10:
                        print a
                        return



main()





                        
