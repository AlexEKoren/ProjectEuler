#Finds the sum of the digits in x factorial

def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def recursion(z):
    if z==1:
        return 1
    else:
        return z*recursion(z-1)

def main(x):
    final=recursion(x)
    i=0
    total=0
    print final
    array=forwardsArray(final)
    print array
    for i in range(len(array)):
        total=total+array[i]
    print total
main(100)
