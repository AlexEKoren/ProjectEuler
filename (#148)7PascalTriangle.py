import time
def pascalsTriangle(rows):
    triangle=[[1]]
    for x in range(1,rows):
        temp=[1]
        for n in range(0,x-1):
            temp.append(triangle[x-1][n]+triangle[x-1][n+1])
        temp.append(1)
        triangle.append(temp)
    return triangle

def main2(a):
    tri=pascalsTriangle(a)
    total=0
    for x in tri:
        tempCount=0
        for y in x:
            if y%7!=0:
                tempCount+=1
        print tri.index(x), tempCount
        total+=tempCount
    print total

def main(a):
    inmul=1
    powmul=1
    total=0
    pows=[7**x for x in range(11)]
    n=1
    for x in range(a):
        if x%7==0 and x!=0:
            n=1
            inmul+=1
            for z in pows:
                if x%z==0:
                    powmul=x/z+1
                    inmul=1
                    break
        #print x, n*inmul*powmul
        total+=n*inmul*powmul
        n+=1
        
    print total

main(343*7+2)
