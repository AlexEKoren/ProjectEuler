import itertools
def main(s, n, t):
    perms=list(itertools.combinations_with_replacement('ABCDEFGHIJKL', 20))
    print perms[0]

main(1,1,1)
