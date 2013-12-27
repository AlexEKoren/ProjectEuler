def main(n):
    x=n
    i=n
    e=10**-7
    while x<n**3:
        #print x
        temp=(x+1)**(1.0/3)
        if int(temp)-e+1<temp<int(temp)+e+1:
            print 'yes', temp
        x+=i
main(78)
