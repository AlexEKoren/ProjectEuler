def main(a):
    for b in range(a):
        array=[]
        for x in range(a/5):
            temp=[]
            for y in range(a/5):
                temp.append(False)
            array.append(temp)
        #print array
        antX=5
        antY=5
        antD=(-1,0)
        for x in range(b):
            #on a white square
            if array[antX][antY]==False:
                #print "yes"
                array[antX][antY]=True
                antD=(antD[1], antD[0]*-1)
                antX+=antD[0]
                antY+=antD[1]
            #on a black square
            else:
                array[antX][antY]=False
                antD=(antD[1]*-1, antD[0])
                antX+=antD[0]
                antY+=antD[1]
            #print antX, antY, antD
        #print array
        totalS=len(array)*len(array[0])
        totalB=0
        for x in array:
            for y in x:
                if y==True:
                    totalB+=1
        print b,totalB, totalS

main(100)
