def findSquares(x):
    array=[]
    for y in range(1,x):
        array.append(y**2)
    return array

def main(a):
    squares=findSquares(a)
    for z in range(2, squares[-1],2):
        for y in range(z+1, squares[-1], 2):
            for x in range(y+1, squares[-1]):
                    if squares.__contains__(x+y):
                        if squares.__contains__(x-y):
                            #print x, y, z
                            if squares.__contains__(x+z):
                                if squares.__contains__(x-z):
                                    print x, y, z
                                    if squares.__contains__(y+z):
                                        if squares.__contains__(y-z):
                                            print "done:", x+y+z
                                            return
main(30)
