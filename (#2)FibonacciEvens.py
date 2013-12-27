'''Finds the even numbered Fibonacci sequence numbers and finds there sum
Values under x'''

def evenSumOfFibonacci(x):
    total=0
    a,b=0,1
    #starting values are 0 and 1
    while b<x:
        #while the fibonacci sequence is less than x
        a, b = b, a+b
        #adds a to be and sets a as b
        if b%2==0:
            #if b is even, adds it to the total
            total=total+b

    print total

evenSumOfFibonacci(4000000)
