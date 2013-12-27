import itertools

r=[str(x) for x in range(10)]

def isPan(x):
    s=str(x)
    if len(s)!=10:
        return False
    for y in r:
        if not y in s:
            return False
    return True

def main():
    for x in range(1,10):
        l=r
        l.remove(str(x))
        
