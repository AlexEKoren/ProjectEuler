#Finds the 4 fractions that can be reduced by cancelling a digit
#in the denominator and the numerator
def forwardArray(a):
    #creates an array of the number by inserting each digit
    f=[]
    a=n
    while(a!=0):
        f.insert(0,a%10)
        a=a/10
    return f

def main():
    numerator=[]
    denominator=[]
    i,j,k,l=1,1,1,1
    while i in range(1,100):
        while j in range(1,100):
            while k in range(1,100):
                while l in range(1,100):
                    numerator.append(i)
                    numerator.append(j)
                    denominator.append(k)
                    denominator.append(l)
                    if numerator[0]==denominator[0]:
                        if j/l==(numerator[0]*10+numerator[1])/(denominator[0]*10+denominator[1]):
                            print numerator
                            print denominator
                    if numerator[1]==denominator[1]:
                        if i/k==(numerator[0]*10+numerator[1])/(denominator[0]*10+denominator[1]):
                            print numerator
                            print denominator
                    if numerator[0]==denominator[1]:
                        if j/k==(numerator[0]*10+numerator[1])/(denominator[0]*10+denominator[1]):
                            print numerator
                            print denominator
                    if numerator[1]==denominator[0]:
                        if i/l==(numerator[0]*10+numerator[1])/(denominator[0]*10+denominator[1]):
                            print numerator
                            print denominator
                    l=l+1
                k=k+1
            j=j+1
        i=i+1
main()
