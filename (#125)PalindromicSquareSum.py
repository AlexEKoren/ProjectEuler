import time
def findSquares(x):
    array=[]
    for y in range(1,x):
        array.append(y**2)
    return array

def isPalindrome(x):
    if str(x)==str(x)[::-1]:
        return True
    return False

def main(x):
    t=time.time()
    total=0
    squares=findSquares(int(x**.5))
    array=[]
    #print time.time()-t
    #print findSquares(10)
    for y in range(0,len(squares)):
        sub=squares[y]
        for z in range(y+1,len(squares)):
            sub+=squares[z]
            if sub>x:
                break
            #print sub
            if isPalindrome(sub):
                array.append(sub)
                total+=sub
                #print sub
        #print "back to y"
    print sum(list(set(array)))
    print time.time()-t

main(10**8)
