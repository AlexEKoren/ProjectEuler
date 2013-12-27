#Returns how many numbers under x are palindromic as decimal numbers and binary

def binary(m) :
    multiplier=0
    total=0
    while m>0:
        if m%2==1:
            total=total+1*(10**multiplier)
        m=m/2
        multiplier=multiplier+1
    return total
            
def forwardsArray(n):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f
    
def backwardsArray(n):
    #creates a backwards array of the number by inserting each digit after the others
    b=[]
    a=n
    while(a!=0):
        b.append(a%10)
        a=a/10
    return b

def main(x):
    i=1
    total=0
    while i<x:
        if forwardsArray(i)==backwardsArray(i) and forwardsArray(binary(i))==backwardsArray(binary(i)):
            total=total+i
        i=i+1
    print total

main(1000000)
