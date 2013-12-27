#Finds the sum of the digits in 2^x

def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def main(x):
    array=forwardsArray(2**x)
    i=0
    total=0
    while i<len(array):
        total=total+array[i]
        i=i+1
    print total

main(1000)
