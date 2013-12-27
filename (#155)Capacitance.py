import itertools
def main(n):
    total=0
    for x in range(n):
        total+=2**x
    print total

main(18)
