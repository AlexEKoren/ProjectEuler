from itertools import *
def main():
    signs=list(product("+-*/", repeat=3))
    para=list(combinations([12,13,23,24,34],3))
    m=0
    for a in range(1,10):
        for b in range(1,10):
            if b==a:
                continue
            for c in range(1,10):
                if c==a or c==b:
                    continue
                for d in range(1,10):
                    array=[]
                    if d==a or d==b or d==c:
                        continue
                    for s in signs:
                        string=str(a)+s[0]+str(b)+s[1]+str(c)+s[2]+str(d)
                        for p in para:
                            temp=string
                            for pa in p:
                                if pa==12:
                                    temp="("+temp[0:temp.index(str(b))+1]+")"+temp[temp.index(str(b))+1:]
                                elif pa==13:
                                    temp="("+temp[0:temp.index(str(c))+1]+")"+temp[temp.index(str(c))+1:]
                                elif pa==23:
                                    temp=temp[0:temp.index(str(b))]+"("+temp[temp.index(str(b)):temp.index(str(c))+1]+")"+temp[temp.index(str(c))+1:]
                                elif pa==24:
                                    temp=temp[0:temp.index(str(b))]+"("+temp[temp.index(str(b)):temp.index(str(d))+1]+")"+temp[temp.index(str(d))+1:]
                                elif pa==34:
                                    temp=temp[0:temp.index(str(c))]+"("+temp[temp.index(str(c)):temp.index(str(d))+1]+")"+temp[temp.index(str(d))+1:]
                            print temp
                            array.append(eval(temp))
                    print array
main()
