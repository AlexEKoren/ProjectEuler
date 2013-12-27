from graphics import *
def findLargest(a,b,c):
    l2=int(3*(a*b*c)**.5)
    win=GraphWin("Window",150,500)
    win.setCoords(0,0,10,l2)
    m=0
    l=a*b*c
    for x in range(1,l2):
        if x%a==0 or x%b==0 or x%c==0:
            continue
        bo=False
        for q1 in range(l):
            if q1*a>x:
                break
            for q2 in range(l):
                if q1*a+q2*b>x:
                    break
                for q3 in range(l):
                    temp=q1*a+q2*b+q3*c
                    #if x==5:
                        #print q1, q2, q3, q1*a+q2*b+q3*c
                    if temp==x:
                        #print q1, q2, q3, x
                        bo=True
                        break
                    elif temp>x:
                        break
                if bo==True:
                    break
            if bo==True:
                break
        if bo==False:
            #print x
            Line(Point(0,x),Point(10,x)).draw(win)
            m=x
    label = Text(Point(5, l2-l2/4), "Max: "+str(m))
    #label.setSize(50)
    label.draw(win)
    label2=Text(Point(5,l2-l2/8), "Primes: "+str(a)+","+str(b)+","+str(c))
    label2.draw(win)
    win.getMouse()
    win.close()
    return m


print findLargest(7,11,29)
