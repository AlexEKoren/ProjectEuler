'''finds the sum of all the numbers that are multiples of 3 and 5 below 1000'''

def sumsofmultiples3and5():
    total=0
    for n in range(1000):
        #while n is less than 1000
        if n%3==0 or n%5==0:
            #if it is a multiple of 3 or 5, add n number to the total
            a=a+n
    print total

sumsofmultiples3and5()
        
