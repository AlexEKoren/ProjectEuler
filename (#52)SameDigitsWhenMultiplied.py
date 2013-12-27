def main():
    x=1
    while 1==1:
        #print x
        two=list(str(2*x))
        two.sort()
        one=list(str(x))
        one.sort()
        if one==two:
            three=list(str(3*x))
            three.sort()
            if one==three:
                four=list(str(4*x))
                four.sort()
                if one==four:
                    five=list(str(5*x))
                    five.sort()
                    if one==five:
                        six=list(str(6*x))
                        six.sort()
                        if one==six:
                            print x
                            return
        x+=1

main()
