"""
Matt Andrews
random_graph function by kaya3 from:
https://stackoverflow.com/questions/60161376/easiest-way-to-generate-an-undirected-graph-s-adjacency-list
with slight alterations, comments, and main() by Matt Andrews
"""
from random import random
from itertools import product, combinations


def random_graph(n, p, *, directed=False):
    nodes = range(n)
    # Base list with specified number of nodes
    adj_list = {i: [] for i in nodes}
    # Set of all 2-node subsets
    possible_edges = product(nodes, repeat=2) if directed else combinations(nodes, 2)
    for u, v in possible_edges:
        if random() < p:  # Select edge based on probability p
            adj_list[u].append(v)
            if not directed: # Add the corresponding edge for undirected graphs
                adj_list[v].append(u)
    return adj_list


def main():
    vertex_num = int(input())

    adj_list = random_graph(vertex_num, 0.5, directed=False)

    print(vertex_num)
    for node in adj_list:
        print(node, end=" ")
        for edge in adj_list[node]:
            print(edge, end=" ")
        print()


if __name__ == "__main__":
    main()
