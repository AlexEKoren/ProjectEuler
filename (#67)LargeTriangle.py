import AEKsys
import time
def main():
    t=time.time()
    f=(open(AEKsys.MyPrograms+ "\\#67triangle.txt","r")).readlines()
    tris=[]
    tri=[]
    triangle=[]
    for l in f:
        tris.append(l.split('\n'))
    for x in tris:
        tri.append(x[:-1])
    for x in tri:
        for y in x:
            triangle.append(y.split(" "))
    tri=[]
    for x in triangle:
        temp=[]
        for y in x:
            temp.append(int(y))
        tri.append(temp)
    while len(tri)>1:
        x=0
        temp=[]
        #print tri[-1], tri[-2]
        while x<len(tri[-1])-1:
            if tri[-1][x]>tri[-1][x+1]:
                temp.append(tri[-1][x]+tri[-2][x])
                #print tri[-1][x], tri[-2][x]
            else:
                temp.append(tri[-1][x+1]+tri[-2][x])
            x+=1
        #print temp
        tri[-2]=temp
        tri=tri[:-1]
    print time.time()-t
    print tri
            

main()
