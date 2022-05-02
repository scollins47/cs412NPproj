from Trace_Calls import Trace_Calls
import time


@Trace_Calls
def bron_kerbosch(R, P, X, graph, find_pivot=False):
    if len(P) == 0:
        if len(X) == 0:

            return R
    else:
        frontier = set(P)
        if find_pivot:
            u = find_max_pivot(graph, P, X)
            frontier = set(P) - set(graph[u])
        for v in frontier:
            bron_kerbosch(
                R.union({v}),
                P.intersection(set(graph[v])),
                X.intersection(set(graph[v])),
                graph,
                find_pivot
             )

            P.remove(v)

            X = X.union({v})

def find_max_pivot(graph, P, X):
    nodes = list(P.union(X))
    u = nodes[0]
    max_intersection = len(set(graph[nodes[0]]).intersection(P))
    for n in nodes:
        if len(set(graph[n]).intersection(P)) > max_intersection:
            u = n
            max_intersection = len(set(graph[n]).intersection(P))

    return u


def bk_initial_call(graph, pivot=False, visualize=False):
    f = bron_kerbosch
    f(set(), set(graph.keys()), set(), graph, pivot)
    print(f.get_recursive_calls())
    g = f.display_records()
    f.reset()
    return g

def N(v, g):
    return [n_v for i, n_v in enumerate(g[v]) if n_v]

def main():
    vertex_num = int(input())
    adj_list = {x: [None] for x in range(vertex_num)}
    for i in range(vertex_num):
        vertex, *edges = input().split()
        vertex = int(vertex)
        edges = [int(edge) for edge in edges]
        if adj_list[vertex] == [None]:
            adj_list[vertex] = edges
        else:
            adj_list[vertex].extend(edges)
    print("Recursive Calls")

    t0 = time.time()
    cliques = bk_initial_call(adj_list)
    print(max(cliques, key=len))
    t1 = time.time() - t0
    print("Time elapsed: ", t1)


if __name__ == '__main__':
    main()

