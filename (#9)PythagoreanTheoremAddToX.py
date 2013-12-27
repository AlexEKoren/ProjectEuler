#finds the triplet of a pythagorean theorem that adds up to 1000
import time
def main(x):
    f1=time.time()
    for a in range(x):
        #goes from 0 to x in "a" values
        for b in range(x):
            #goes from 0 to x in "b" values at a constant "a" value
            c=(a**2+b**2)**.5
            #finds c by using pythagorean theorem
            if a+b+c==x and a*b*c!=0:
            #if they add up to x and none of them are 0 (making it not a triangle)
                print a*b*c
                print a
                print b
                print c
                f2=time.time()
                print f2-f1
                return
main(1000)

    
