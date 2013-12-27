#Finds the number of letters in all numbers up to x (below 10000
def thousands(t):
    singles=[0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens=[3, 6, 6, 8, 8, 7, 7, 9, 9, 8]
    doubleDigits=[6, 6, 6, 5, 5, 7, 7, 6]
    thousand=t
    thousand=thousand/1000
    if(thousand==0):
        return 0
    else:
        return singles[thousand]+8;


def hundreds(h):
    singles=[0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens=[3, 6, 6, 8, 8, 7, 7, 9, 9, 8]
    doubleDigits=[6, 6, 6, 5, 5, 7, 7, 6]
    hundred=h
    hundred=hundred/100%10;
    if hundred==0:
        return 0
    else:
        return singles[hundred]+7;
    
def doubleDigits(dd):
    singles=[0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
    teens=[3, 6, 6, 8, 8, 7, 7, 9, 9, 8]
    doubleDigits=[6, 6, 6, 5, 5, 7, 7, 6]
    doubleDigit=dd%100
    if(dd>99):
        if(doubleDigit>=10 and doubleDigit<=19):
            return 3+teens[doubleDigit-10]
        elif(doubleDigit>0 and doubleDigit<=9):
            return 3+singles[doubleDigit]
        elif(doubleDigit>=20 and doubleDigit<=99):
            return 3+doubleDigits[doubleDigit/10-2]+singles[doubleDigit%10]
        elif(doubleDigit==0):
            return 0
        else:
            return 0
    elif(dd<99):
        if(doubleDigit>=10 and doubleDigit<=19):
            return teens[doubleDigit-10]
        elif(doubleDigit>0 and doubleDigit<=9):
            return singles[doubleDigit]
        elif(doubleDigit>=20 and doubleDigit<=99):
            return doubleDigits[doubleDigit/10-2]+singles[doubleDigit%10]
        elif(doubleDigit==0):
            return 0
        else:
            return 0
    else:
        return 0


def findNumberOfLetters(x):
    total=0
    subtotal=0
    i=0
    for i in range(0,x+1):
        subtotal=thousands(i)+hundreds(i)+doubleDigits(i)
        total=total+subtotal
        subtotal=0
    print total
    
findNumberOfLetters(19)      
