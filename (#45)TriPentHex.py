#Finds the first haxagonal, triangle, and pentagonal number over 40755
def createTriangle():
    i=1
    Triarray=[]
    while i<100000:
        Triarray.append((i*(i+1))/2)
        i=i+1
    return Triarray

def isHexagonal():
    i=1
    Hexarray=[]
    while i<100000:
        Hexarray.append(i*(2*i-1))
        i=i+1
    return Hexarray

def isPentagonal():
    i=1
    Pentarray=[]
    while i<100000:
        Pentarray.append((i*(3*i-1))/2)
        i=i+1
    return Pentarray
    
def main():
    pent=isPentagonal()
    hexa=isHexagonal()
    tri=createTriangle()
    k=286
    while k<99999:
        a=hexa[k]
        if pent.__contains__(a) and tri.__contains__(a):
            print hexa[k]
            return
        k=k+1

main()
