pastFills=[]
answers=[]
def F(size,blocks):
    if blocks<size:
        return 1
    if blocks==size:
        return 2
    if [size,blocks] in pastFills:
        return answers[pastFills.index([size,blocks])]
    total=1
    for x in range(size,blocks+1):
        for y in range(blocks-x+1):
            total+=F(size, blocks-(x+y+1))
    pastFills.append([size,blocks])
    answers.append(total)
    return total


def main(a,s):
    x=F(s,s+1)
    blocks=s+1
    while x<a:
        blocks+=1
        x=F(s,blocks)
    print blocks

main(10**6,50)



