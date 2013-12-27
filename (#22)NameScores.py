import AEKsys

def main():
    f=(open(AEKsys.MyPrograms+ "\\#14names.txt","r")).readlines()
    nameList=f[0].split(',')
    names=[]
    total=0
    j=1
    i=0
    namescore=0
    for nom in nameList:
        names.append(nom[1:len(nom)-1])
    names.sort()
    for n in names:
        while i in range(len(n)):
            namescore=(ord(n[i])-64)+namescore
            i=i+1
        i=0
        total=total+namescore*j
        namescore=0
        j=j+1
    print total
main()

