from decimal import *
def main():
    j=11
    i=21
    while i<100:
        while j<100:
            if str(i)[1]=="0" or str(j)[1]=="0":
                print "0's"
            elif i==j:
                print "equal"
            elif str(i)[1]==str(j)[0]:
                if ((i/10)/((j%10)*1.0))==(i/(j*1.0)):
                    #print "first"
                    print i, j
            elif str(i)[0]==str(j)[1]:
                if ((i%10)/((j/10)*1.0))==(i/(j*1.0)):
                    #print "second"
                    print i, j
            elif str(i)[1]==str(j)[1]:
                if ((i/10)/((j/10)*1.0))==(i/(j*1.0)):
                    #print "third"
                    print i, j
            j=j+1
        j=11
        i=i+1
main()
