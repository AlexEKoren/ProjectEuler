import time
def main(y):
    t=time.time()
    array89=[89]
    array1=[1]
    x=2
    counter=0
    while x<648  :
        subtotal=0
        temp=x
        while 1==1:
            subtotal=sum(int(q)**2 for q in str(temp))
            temp=subtotal
            if array89.__contains__(temp):
                temp=89
                counter=counter+1
                array89.append(x)
                break
            if array1.__contains__(temp):
                temp=1
                array1.append(x)
                break
        x=x+1
    while x<y:
        subtotal=0
        temp=x
        while 1==1:
            subtotal=sum(int(q)**2 for q in str(temp))
            temp=subtotal
            if array89.__contains__(temp):
                temp=89
                counter=counter+1
                break
            if array1.__contains__(temp):
                temp=1
                break
        x=x+1
    t2=time.time()
    print t2-t
    print counter
main(10000000)

        
