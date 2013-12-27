def findPows(x):
    p=[]
    n=2
    y=0
    while n**y<x:
        p.append(n**y)
        y+=1
    return p
    
def main(x):
    p=findPows(x)
    a=x
    adds=[]
    for y in reversed(p):    
        while a-y>=0:
            adds.append(y)
            a-=y
    print adds, a
    
main(10**25)
