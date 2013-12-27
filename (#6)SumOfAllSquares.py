#finds the difference between the sum of all the square numbers with roots below 100

def main(n):
    sumOfRootsSquared=0
    sumOfAllSquares=0
    x=0
    while x<n+1:
        #while x is less than or equal to limit n
        sumOfRootsSquared=sumOfRootsSquared+x
        #add it to the sumOfRoots
        x=x+1
    sumOfRootsSquared=sumOfRootsSquared**2
    #squares the sumOfRoots
    x=0
    #resets x
    while x<n+1:
        #while x is less than or equal to limit n
        sumOfAllSquares=sumOfAllSquares+x**2
        #adds x squared to the sum of all the squares
        x=x+1

    print sumOfRootsSquared-sumOfAllSquares
    #prints the difference

main(10)
