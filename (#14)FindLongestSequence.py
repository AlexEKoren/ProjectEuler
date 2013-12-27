#Finds the longest chain of the sequence by starting at a number beneath 1 million

def main():
    array=[]
    i=999999
    final=[]
    while i>750000:
        if (i-1%3)==0:
            i=i-2
        j=i
        print i
        while i>0:
            array.append(i)
            if i<=0:
                break
            elif i==1:
                if len(array)>len(final):
                    final=array
                    break
            elif i%2==0:
                i=i/2
            else:
                i=3*i+1
        array=[]
        i=j-2

    print final
    
main()
        
