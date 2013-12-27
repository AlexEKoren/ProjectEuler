def main(x):
    count=0
    for a in range(1,x):
        for b in range(1,a):
            for c in range(b+1,x):
                if a+b+c>x:
                    break
                else:
                    if a==2 and b==1 and c==5:
                        print "yes", a, b, c
                        print ((a+b*(c**.5))**(1.0/3))
                        print (((a-b*-1*(c**.5))**(1.0/3))*-1)
                    if (a+b*(c**.5))**(1.0/3)+(a-(b*-1*(c**.5)))**(1.0/3)==0:
                        count+=1
                        print a, b, c
main(1000)
