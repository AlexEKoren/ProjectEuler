def main():
    x=11
    m=0
    final=0
    while x<10000:
        temp=x
        while m<50:
            if int(str(x)[::-1])+x==int(str(int(str(x)[::-1])+x)[::-1]):
                break
            else:
                m=m+1
                x=x+int(str(x)[::-1])
        if m==50:
            final=final+1
        m=0
        x=temp+1
    
    print final
main()
