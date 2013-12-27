def createPic(n):
    pic=[]
    for y in range(n):
        temp=[]
        for x in range(n):
            if (x*2**(n-1))**2+(y*2**(n-1))**2<=2**(2*n-2):
                temp.append(True)
            else:
                temp.append(False)
        pic.append(temp)
    pic[0][0]=pic[n-1][0]
    return pic

pic=[[False,False],[True,False]]
def rec(x1,x2,y1,y2):
    print x1, x2, y1, y2
    if x1==x2-1 or x1==x2:
        return 2
    else:
        br=False
        count=0
        b="no"
        for y in range(y1,y2):
            for x in range(x1,x2):
                if pic[y][x]==False:
                    if b==True:
                        print "yes"
                        print x, y
                        count+=rec(x1,(x2+x1)/2,y1,(y2+y1)/2)
                        count+=rec((x2+x1)/2,x2,y1,(y2+y1)/2)
                        count+=rec(x1,(x2+x1)/2,(y2+y1)/2,y2)
                        count+=rec((x2+x1)/2,x1,(y2+y1)/2,y2)
                        br=True
                    b=False
                elif pic[y][x]==True:
                    if b==False:
                        print "yes"
                        print x, y
                        count+=rec(x1,(x2+x1)/2,y1,(y2+y1)/2)
                        count+=rec((x2+x1)/2,x2,y1,(y2+y1)/2)
                        count+=rec(x1,(x2+x1)/2,(y2+y1)/2,y2)
                        count+=rec((x2+x1)/2,x1,(y2+y1)/2,y2)
                        br=True
                    b=True
        if br==False:
            count=2
        else:
            count+=1
        return count
print rec(0,2,0,2)

                
