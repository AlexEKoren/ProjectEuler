def cube(x):
    cubes=[]
    for y in range(2,x):
        cubes.append(y**3)
    return cubes
def square(x):
    squares=[]
    for y in range(2, x):
        squares.append(y**2)
    return squares

def main(z):
    cubes=cube(z)
    squares=square(z*20)
    pals=[]
    total=0
    for x in xrange(int(z**3.1)):
        if str(x)==str(x)[::-1]:
            pals.append(x)
    palVal=[0]*len(pals)
    print "pals done", len(pals)#, pals
    for x in squares:
        for y in cubes:
            if (x+y) in pals:
                #print x+y
                palVal[pals.index(x+y)]+=1
                if palVal[pals.index(x+y)]==4:
                    total+=x+y
                    print x+y, x, y
    #print pals
main(220)
                
