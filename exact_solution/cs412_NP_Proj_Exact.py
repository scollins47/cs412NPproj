"""
Matt Andrews
"""


def max_clique(graph):
    max_count = 0
    out_clique = set()
    
    for vertex in graph:
        running_count = 0
        possibles = list(graph.keys())
        # print(possibles)
        possibles.remove(vertex)
        clique = [vertex]
        running_count += 1
        for possible in possibles:
            # print("TRYING {}".format(possible))
            add_vert = True
            for included in clique:
                if graph[included] is None or possible not in graph[included]:
                    add_vert = False
                    break
            # print("ADD? {}".format(add_vert))
            if add_vert:
                clique.append(possible)
                running_count += 1
                    
        if running_count > max_count:
            # print("NEW MAX: {}".format(clique))
            max_count = running_count
            out_clique = clique
            
    return out_clique
        

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

    output = max_clique(adj_list)
    print(output)
    
    
if __name__ == "__main__":
    main()
