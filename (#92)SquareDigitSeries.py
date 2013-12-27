import time
def main(y):
    t=time.time()
    x=100
    counter=80
    array89=[89]
    array1=[1]
    while x<y:
        '''cont=False
        tempq=0
        while cont==False:
            for q in str(x):
                if not int(q)>tempq:
                    print x
                    x=x+1
                    break
                if str(x).index(q)==len(str(x))-1:
                    cont=True'''
        temp=x
        while temp!=1 and temp!=89:
            subtotal=0
            for l in str(temp):
                subtotal=subtotal+int(l)**2
                temp=subtotal
            if array89.__contains__(temp):
                temp=89
            if array1.__contains__(temp):
                temp=1
        if temp==89:
            #print x
            counter=counter+1
            if x<375 and not array89.__contains__(x):
                array89.append(x)
        if temp==1:
            if x<375 and not array1.__contains__(x):
                array1.append(x)
        x=x+1
    t2=time.time()
    print t2-t
    print counter
main(100000)
