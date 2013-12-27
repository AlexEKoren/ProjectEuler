def main(limit):
    l2=limit*2
    l2d=limit/2
    final=[l2 for x in range(limit+1)]
    for a in range(1,l2d/2056):
     for b in range(a,l2d/1024):
      if a*b>l2:
          break
      for c in range(b,l2d/512):
        if a*b*c>l2:
            break
        for d in range(c,l2d/256):
          if a*b*c*d>l2:
              break
          for e in range(d,l2d/128):
            if a*b*c*d*e>l2:
                break
            for f in range(e,l2d/64):
              if a*b*c*d*e*f>l2:
                  break
              for g in range(f,l2d/32):
                if a*b*c*d*e*f*g>l2:
                    break
                for h in range(g,l2d/16):
                  if a*b*c*d*e*f*g*h>l2:
                    break
                  for i in range(h,l2d/8):
                    if a*b*c*d*e*f*g*h*i>l2:
                        break
                    for j in range(i,l2d/4):
                      if a*b*c*d*e*f*g*h*i*j>l2:
                          break
                      for k in range(j,l2d/2):
                        if a*b*c*d*e*f*g*h*i*j*k>l2:
                         break
                        for l in range(k,l2d):
                          if a*b*c*d*e*f*g*h*i*j*k*l>l2:
                              break
                          for m in range(l,l2d):
                            if a*b*c*d*e*f*g*h*i*j*k*l*m<l2:
                                mul=a*b*c*d*e*f*g*h*i*j*k*l*m
                                s=a+b+c+d+e+f+g+h+i+j+k+l+m
                                if mul-s+13<=limit:
                                    if final[mul-s+13]>mul:
                                        final[mul-s+13]=mul
    print sum(set(final))
                                
main(12000)
