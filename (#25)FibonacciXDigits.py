#Finds the first Fibonacci sequence number to have x digits

def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def main(x):
    c=0
    a,b=0,1
    i=1
    array=[]
    while len(array)<x:
        a, b = b, a+b
        i=i+1
        array=forwardsArray(b)
    print i

main(2)
    
