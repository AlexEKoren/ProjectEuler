def rotate(dire, x, y):
    if dire=="ccw":
        return y*-1,x
    else:
        return y,x*-1

def copy(a):
    l=[]
    for x in a:
        l.append(x)
    return l

def b(g):
    count=0
    for x in g:
        for y in x:
            if not y:
                count+=1
    return count

def main(a,r,c):
    row=[]
    for x in range(r):
        row.append(True)
    grid=[]
    for x in range(c):
        grid.append(copy(row))
    antX=10
    antY=10
    dirX=1
    dirY=0
    print len(grid)*len(grid[0])
    for x in range(a):
        if grid[antX][antY]:
            grid[antX][antY]=False
            dirX,dirY=rotate("cw",dirX,dirY)
            antX+=dirX
            antY+=dirY
        else:
            grid[antX][antY]=True
            dirX,dirY=rotate("ccw",dirX,dirY)
            antX+=dirX
            antY+=dirY
        print b(grid)
    count=0
    for x in grid:
        for y in x:
            if not y:
                count+=1
    print count

main(100,100,100)
