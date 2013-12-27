from math import *
def findVertex(angle):
    y=(sin(angle)*20)**2*-1/(2*-9.8)+100
    t=sin(angle)*-20/-9.8
    x=20*cos(angle)*t
    return x, y

def drange(start, stop, step):
     r = start
     while r < stop:
             yield r
             r += step
             
def main():
    arrayX=[]
    arrayY=[]
    for x in drange(0,pi/2,.01):
        arrayX.append(findVertex(x)[0])
        arrayY.append(findVertex(x)[1])
    total=0
    for y in arrayY:
        
            
    
    
