def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def main():
    i=1
    total=0
    while i<1001:
        total=total+(i**i)
        i=i+1
    print total
    array=forwardsArray(total)
    print array[len(array)-10:len(array)]

main()
