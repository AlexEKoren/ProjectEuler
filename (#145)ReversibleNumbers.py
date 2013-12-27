def reverse(x):
    return int(str(x)[::-1])

def isOdd(x):
    for l in str(x):
        if not int(l)%2==1:
            return False
    return True
def main():
    final=0
    x=1
    while x<10000000:
        while (int(str(x)[0])%2==int(str(x)[-1])%2) or (int(str(x)[0])%2==int(str(x)[-1])%2):
            x+=1
        if isOdd(x+reverse(x)):
            temp=str(x)
            if int(temp[0])==0 or int(temp[-1])==0:
                final+=0
            else:
                #print temp[0],temp[-1],x, x+reverse(x)
                final+=1
        x+=1
    print final
main()
