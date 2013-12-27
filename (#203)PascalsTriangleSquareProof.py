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

def Primes(x):
    prime=[2]
    z=3
    while z<x**.5:
        isPrime=True
        for y in range(2, int(z**.5)):
            if z%y==0:
                isPrime=False
                break
        if isPrime==True:
            prime.append(z)
        z+=2
    return prime

def Squares(primes):
    square=[]
    for x in primes:
        square.append(x**2)
    return square

def squareProof(num,primes,squares):
    proof=True
    for x in squares:
        if num%x==0:
            proof=False
            break
    if proof==True:
        return True
    else:
        return False
     
def main():
    t=time.time()
    total=0
    array=[]
    triangle=pascalsTriangle(51)
    for x in triangle:
        for y in x:
            array.append(y)
    array=list(set(array))
    array.sort()
    print len(array)
    print "pascal done", time.time()-t
    primes=Primes(array[-1]**.5)
    print "primes done", time.time()-t
    squares=Squares(primes)
    print "squares done", time.time()-t
    for x in array:
        if squareProof(x,primes,squares)==True:
            total+=x
            print x
    print total
main()
        
        
