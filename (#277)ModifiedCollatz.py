import time
def main(a,b):
    t=time.time()
    x=10**a
    l=len(b)
    p=27
    c=3
    num1=0
    num2=0
    changeC=False
    done1=False
    while 1:
        temp=x
        s=""
        while temp!=1:
            if temp%3==0:
                s+="D"
                temp=temp/3
            elif temp%3==1:
                s+="U"
                temp=(temp*4+2)/3
            else:
                s+="d"
                temp=(temp*2-1)/3
            if s==b[0:p*-1]:
                if done1==False:
                    num1=x
                    done1=True
                elif done1==True:
                    num2=x
                    changeC=True
                if changeC==True:
                    changeC=False
                    done1=False
                    c=num2-num1
                    p-=1
            if len(s)>l:
                break
            if s==b:
                print time.time()-t
                print x
                return
        x+=c
main(15, "UDDDUdddDDUDDddDdDddDDUDDdUUDd")
            
            
