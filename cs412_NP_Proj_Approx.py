"""
    name:  Hafet Abdulle, Sammy Collins, Matt Andrews, Kory Erdmann

"""
# All modules for CS 412 must include a main method that allows it
# to imported and invoked from other python scripts
#
from collections import deque
import random
from random import random
from itertools import product, combinations


def main():
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(m)]

    l = [[0] * n for i in range(n)]
    for v in p:
        l[v[0] - 1][v[1] - 1] = 1
        l[v[1] - 1][v[0] - 1] = 1  # Erase if it is a directed graph

    mat = {
        i: set(num for num, j in enumerate(row) if j)
        for i, row in enumerate(l)


    }
    f = mat.keys()
    print()







adj_matrix = [
        [0, 1, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1, 1],
        [1, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]
N = {
    i: set(num for num, j in enumerate(row) if j)
    for i, row in enumerate(adj_matrix)
}

print(N)


# {0: {1, 4}, 1: {0, 2, 4}, 2: {1, 3}, 3: {2, 4, 5}, 4: {0, 1, 3}, 5: {3}}
def BronKerbosch1(P, R=None, X=None):
    P = set(P)
    R = set() if R is None else R
    X = set() if X is None else X
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch1(
            P=P.intersection(N[v]), R=R.union([v]), X=X.intersection(N[v]))
        X.add(v)

if __name__ == "__main__":
    main()
