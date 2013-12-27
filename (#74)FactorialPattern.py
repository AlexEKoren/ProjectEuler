import math
def main():
    x=12
    counter=0
    array=[]
    while x<1000000:
        array=[]
        if x==1000:
            print time.time()-t
            print "1000"
        if x==10000:
            print time.time()-t
            print "10000"
        if x==500000:
            print time.time()-t
            print "half"
        #print x
        y=str(x)
        #print y
        count=0
        while not array.__contains__(y):
            array.append(y)
            fact=0
            #print y
            for b in y:
                fact+=math.factorial(int(b))
            count+=1
            y=str(fact)
            #print y
            if count==60:
                #print count
                counter+=1
                #print "counter plus 1"
                break
        #print x, count
        x+=1
        #print x
    print counter
main()
        
        
