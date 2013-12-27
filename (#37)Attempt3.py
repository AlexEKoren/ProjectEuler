import time
def isPrime(n):
    if n<2:
        #checks if its less than 2
        return False
    if n==2:
        #2 is the first prime number
        return True
    if n%2==0:
        return False
    for x in range(3,int(n**0.5)+1,2):
        #checks if it has any factors beneath its square root plus 1
        if n%x==0:
            return False
    return True
    #returns true if all else is false.

def main():
    x=23
    totalTP=0
    total=0
    while totalTP<11:
        #while not str(x).startswith("2") or str(x).startswith("3") or str(x).startswith("5") or str(x).startswith("7"):
            #x+=1
        temp=x
        cont=True
        while temp>0:
            if isPrime(temp):
                temp/=10
            else:
                cont=False
                break
        #print "first loop done"
        temp=x
        if cont==True:
            while temp>0:
                if not isPrime(temp):
                    cont=False
                    break
                temp=temp%(10**(len(str(temp))-1))
        #print "second loop done"
        #print cont, x
        if cont==True:
            totalTP+=1
            print x, totalTP
            total+=x
        x+=1
    print total
main()
                
                    
                    
