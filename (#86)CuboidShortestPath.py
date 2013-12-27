from math import *
def drange(start, stop, step):
     r = start
     while r < stop:
             yield r
             r += step
             
def isSqr(x):
    return sqrt(x).is_integer()

def main(x, y, z):
     a=z*x*1.0/(z+y)
     a2=y*x*1.0/(z+y)
     #print x, y, z, a
     num=(sqrt((x-a)**2+y**2)+sqrt(a**2+z**2))
     if abs(int(num)-num)<10**-5:
          #print x, y, z, a
          return 1
     num2=(sqrt((x-a2)**2+y**2)+sqrt(a2**2+z**2))
     if abs(int(num2)-num2)<10**-5:
          return 1
     return 0

#main(6,5,3)
count=0
total=0
m=2
s=1
while count<10**5:
     for x in range(s,m):
          for y in range(1,x+1):
               for z in range(1,y+1):
                    #main(x,y,z)
                    count+=main(x,y,z)
     m+=1
     s+=1
     #print m, s, count
print count, m-2
