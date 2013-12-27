import itertools
import time
def all_perms(s):
    counter=0
    if len(s) <=1:
        return s
    else:
        for perm in all_perms(s[1:]):
            for i in range(len(perm)+1):
                counter+=1

def main():
    print all_perms("uuuuuuuuuuuuuuuuuuuudddddddddddddddddddd")
main()
