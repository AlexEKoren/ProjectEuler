def S(m):
    y=1
    maximum=0
    fy=0
    while m/y>0:
        if (m/y)**((y*(y+1))/2)>maximum:
            maximum=(m/y)**((y*(y+1))/2)
            fy=y
        y+=1
    print maximum, fy

S(10)
            
