def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def isPrime(n):
    if n < 2:
        #checks if its less than 2
        return False
    if n == 2:
        #2 is the first prime number
        return True    
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True
    

def main():
    i=1000
    difference=1
    while difference<334:
        while i<9998:
            first=i
            second=i+difference
            third=i+difference*2
            if isPrime(first) and isPrime(second) and isPrime(third):
                array1=forwardsArray(first)
                array2=forwardsArray(second)
                array3=forwardsArray(third)
                print array1
                k=0
                while k<3:
                    if not array2.__contains__(array1[k]):
                        k=0
                        break
                    k=k+1
                if k==3:
                    k=0
                    j=0
                    while j<3:
                        if not array3.__contains__(array1[k]):
                            j=0
                            break
                        j=j+1
                    if j==3:
                        print i
                        print difference
                        return
            i=i+1
        i=1000
        difference=difference+1
main()
