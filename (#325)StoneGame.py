def main(x):
    b=3
    final=0
    a=2
    while b<=x:
        a=1
        while a<b:
            if b-a==1:
                final=final+a+b
                print a, b, final
            elif a%2==0 and a>b/2 and b%2==0:
                final=final+a+b
                print a, b, final
            elif not b<=4 and b-a==2:
                final=final+a+b
                print a, b, final
            elif b%a!=0 and (a+a)%(b-a)==0:
                temp=a
                while a<b:
                    if not (a+a)%(b-a)==0:
                        break
                    else:
                        a=a+temp
                if a>=b:
                    final=final+temp+b
                    print temp,b,final
                a=temp
            a=a+1
        b=b+1
    print final
main(10)
