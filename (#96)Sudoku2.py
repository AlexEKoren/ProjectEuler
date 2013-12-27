import AEKsys, time
def isInt(x):
    try:
        x+1
        return True
    except:
        return False

def row(puzzle,y):
    r=[]
    for x in puzzle[y]:
        if isInt(x):
            r.append(x)
    return r

def column(puzzle,x):
    c=[]
    for y in puzzle:
        if isInt(y[x]):
            c.append(y[x])
    return c

def box(puzzle,y,x):
    b=[]
    for r in range(y/3*3,y/3*3+3):
        for c in range(x/3*3,x/3*3+3):
            if isInt(puzzle[r][c]):
                b.append(puzzle[r][c])
    return b

def pos(puzzle):
    puz=[]
    for y in range(len(puzzle)):
        newrow=[]
        for x in range(len(puzzle)):
            if isInt(puzzle[y][x]):
                newrow.append(puzzle[y][x])
            else:
                p=list(range(1,10))
                for r in row(puzzle,y):
                    if r in p:
                        p.remove(r)
                for c in column(puzzle,x):
                    if c in p:
                        p.remove(c)
                for b in box(puzzle,y,x):
                    if b in p:
                        p.remove(b)
                if len(p)==1:
                    newrow.append(p[0])
                else:
                    newrow.append(p)
        puz.append(newrow)
    return puz
total=0

def isConsistent(puzzle):
    for y in range(len(puzzle)):
        if len(row(puzzle,y))==len(list(set(row(puzzle,y)))):
            for x in range(len(puzzle)):
                 if len(box(puzzle,y,x))==len(list(set(box(puzzle,y,x)))):
                    continue
                 else:
                    return False
        else:
            return False
    for x in range(len(puzzle)):
        if len(column(puzzle,x))==len(list(set(column(puzzle,x)))):
            continue
        else:
            return False
    return True

def format_puzzle(puz):
    for y in puz:
        for x in y:
            print x,
        print
        
def solve(puzzle):
    global total
    if isConsistent(puzzle):
        for y in range(len(puzzle)):
            for x in range(len(puzzle[y])):
                if not isInt(puzzle[y][x]):
                    for z in puzzle[y][x]:
                        new=puzzle[:]
                        new[y][x]=z
                        if solve(pos(new))==True:
                            return True
                    return False
        total+=puzzle[0][0]*100+puzzle[0][1]*10+puzzle[0][2]
        format_puzzle(puzzle)
        return True
    return False

def main():
    f=(open(AEKsys.MyPrograms+"\\sudoku.txt","r")).readlines()
    count=0
    temp=[]
    puzzles=[]
    puz=[]
    count=0
    for x in f:
        if count%10==0:
            if count!=0:
                puzzles.append(puz)
                puz=[]
            count+=1
            continue
        puz.append(list(x[:9]))
        count+=1
    puzzles.append(puz)
    nums=[]
    for x in range(1,10):
        nums.append(x)
    for p in puzzles:
        puz=[]
        for x in p:
            row=[]
            for y in x:
                if y=='0':
                    row.append(nums[:])
                else:
                    row.append(int(y))
            puz.append(row)
        solve(pos(puz))
        print total, puzzles.index(p)+1
    print total
                    
t=time.time()          
main()
print time.time()-t


        
