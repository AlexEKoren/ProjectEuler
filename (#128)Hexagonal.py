def isPrime(x):
    if x%2==0:
        return False
    for y in range(3,int(x**.5)+1,2):
        if x%y==0:
            return False
    return True

def gen():
    i=6
    c=2
    while True:
        temp=[]
        lim=c+i
        while c<lim:
            temp.append(c)
            c+=1
            
        yield temp
        i+=6

def main():
    g=gen()
    hexs=[[],[]]
    hexs.append(g.next())
    hexs.append(g.next())
    hexs.append(g.next())
    total=0
    ring=3
    while total<2000:
        for x in range(len(hexs[ring])):
            count=0
            num=hexs[ring][x]
            if x==0:
                U=(ring-1)*6
                if isPrime(U-1):
                    count+=1
                if isPrime(2*U+5):
                    count+=1
                if isPrime(U+1):
                    count+=1
            elif x==len(hexs[ring])-1:
                if isPrime(num-hexs[ring][0]):
                    count+=1
                if isPrime(num-hexs[ring][0]-1):
                    count+=1
                if isPrime(num-(hexs[ring][0]-(ring-2)*6)):
                    count+=1
                if isPrime(ring*6-1):
                    count+=1
            else:
                if x%ring==0:
                    temp=hexs[ring+1][x+1]
                    if isPrime(temp-num):
                        count+=1
                    if isPrime(temp-num+1):
                        count+=1
                    if isPrime(temp-num-1):
                        count+=1
                    if isPrime((ring-2)*6+1):
                        count+=1
                else:
                    pos=x%(ring-1)+x/(ring-1)*(ring-2)-1
                    temp=hexs[ring-1][pos]
                    if isPrime(num-temp):
                        count+=1
                    if isPrime(num-temp+1):
                        count+=1
                    pos=x%(ring-1)+x/(ring-1)*ring
                    temp=hexs[ring+1][pos]
                    if isPrime(temp-num):
                        count+=1
                    if isPrime(temp-num+1):
                        count+=1
            if count==3:
                print num, total+1
                total+=1
                if total>=2000:
                    return
        hexs.append(g.next())
        ring+=1

main()
                
            
