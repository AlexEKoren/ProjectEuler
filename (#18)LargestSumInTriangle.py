#Finds the largest sum traveling up the triangle
#NEEDS WORK

def findLargest(z):
    array=z
    i=0
    largest=0
    while i in range(len(array)):
        if array[i]>largest:
            largest=array[i]
        i=i+1
    print largest
    return largest

def main():
    total=0
    a=[
        4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    b=[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
    c=[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
    d=[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
    e=[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
    f=[41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
    g=[41, 41, 26, 56, 83, 40, 80, 70, 33]
    h=[99, 65, 4, 28, 6, 16, 70, 92]
    i=[88, 2, 77, 73, 7, 63, 67]
    j=[19, 1, 23, 75, 3, 34]
    k=[20, 4, 82, 47, 65]
    l=[18, 35, 87, 10]
    m=[17, 47, 82]
    n=[95, 64]
    o=[75]
    total=findLargest(a)+findLargest(b)+findLargest(c)+findLargest(d)
    total=total+findLargest(e)+findLargest(f)+findLargest(g)+findLargest(h)
    total=total+findLargest(i)+findLargest(j)+findLargest(k)+findLargest(l)
    total=total+findLargest(m)+findLargest(n)+findLargest(o)
    print total

main()
