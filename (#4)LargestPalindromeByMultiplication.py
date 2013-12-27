#Finds the largest number palindrome of 2, 3 digit numbers

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

    
def main():
    x=0
    #the number being checked for being a palindrome
    final=0
    #final number
    i=100
    j=100
    #counting variables
    for i in range(100,1000):
        for j in range(100,1000):
            #nested for loop
            x=i*j
            #multiplies the numbers in each loop
            if backwardsArray(x)==forwardsArray(x) and x>final:
                #if the number is a palindrome (backwards=forwards) and its greater than the previous largest palindrome, set it as final
                final=x
            

    print final

main()


            
                
            
            
            
