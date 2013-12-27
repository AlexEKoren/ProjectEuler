import AEKsys

def createTriangle(x):
    i=1
    Triarray=[]
    while i<x:
        Triarray.append((i*(i+1))/2)
        i=i+1
    print Triarray
    return Triarray

def main():
    final=0
    array=createTriangle(50)
    f=(open(AEKsys.MyPrograms+ "\\#42names.txt","r")).readlines()
    wordList=f[0].split(',')
    words=[]
    i=0
    wordscore=0
    for word in wordList:
        words.append(word[1:len(word)-1])
    for n in words:
        while i in range(len(n)):
            wordscore=(ord(n[i])-64)+wordscore
            i=i+1
        if array.__contains__(wordscore):
            final=final+1
        wordscore=0
        i=0
    print final

main()
