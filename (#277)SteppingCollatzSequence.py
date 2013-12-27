def main(y):
    final=""
    check="UDDDUdddDDUDDddDdDddDDUDDdUUDd"
    x=y
    maxL=0
    num1=0
    num2=0
    mod=3
    modA=1
    while final!=check:
        if final=="":
            temp=x
        if temp%3==0:
            temp/=3
            final+="D"
        elif temp%3==1:
            temp*=4
            temp+=2
            temp/=3
            final+="U"
        else:
            temp*=2
            temp-=1
            temp/=3
            final+="d"
        if not check[0:len(final)]==final:
            if len(final)>maxL:
                maxL=len(final)
                num1=x
            elif len(final)==maxL and num2<num1:
                num2=x
            if num2-num1!=mod and num2>num1:
                mod=num2-num1
                print "mod change", mod, modA
                modA=num1%mod
            x+=1
            print final, check, x-1, mod, modA
            final=""
            while x%mod!=modA:
                x+=1
        if len(final)==len(check):
            break
    print x
main(10**15+1)
