def layer(x,y,z,l):
    if l>1:
        print layer(x,y,z*2,l-1), y*2, x*2, 4*((l-1)*2-1)
        return layer(x,y,z*2,l-1)+y*2+x*2+4*((l-1)*2-1)
    else:
        return x*y*2+y*z*2+x*z*2

print layer(5,1,1,2)
