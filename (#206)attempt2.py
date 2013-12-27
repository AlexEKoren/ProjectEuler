def main():
    x=1009950430
    b=True
    while len(str(x**2))<20:
        if (str(x**2))[0]==1:
            print "level 1", x**2
            if (str(x**2))[2]==2:
                print "level 2", x**2
                if (str(x**2))[4]==3:
                    print "level 3", x**2
                    if (str(x**2))[6]==4:
                        print "level 4", x**2
                        if str((x**2))[8]==5:
                            print "level 5", x**2
                            if (str(x**2))[10]==6:
                                print "level 6", x**2
                                if (str(x**2))[12]==7:
                                    print "level 7", x**2
                                    if (str(x**2))[14]==8:
                                        print "level 8", x**2
                                        if (str(x**2))[16]==9:
                                            print "level 9", x**2
                                            if (str(x**2))[18]==0:
                                                print x
                                                return
        if b==True:
            x+=40
            b=False
        else:
            x+=60
            b=True
        #print x**2, x
        print str(x**2)[0], str(x**2)[2], str(x**2)[4]
main()
