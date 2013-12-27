def c(x):
    cubes=[]
    for y in range(x):
        cubes.append(y**3)
    return cubes

def main(a):
    cube=c(a)
    cubes=[]
    for x in cube:
        cubes.append([x,list(str(x))])
    for x in cubes:
        x[1].sort()
    for x in cubes:
        count=0
        #print x[0]
        for y in range(cubes.index(x), len(cubes)):
            if x[1]==cubes[y][1]:
                count+=1
        if count==5:
            print x[0]
            break
main(10000)
            
                
