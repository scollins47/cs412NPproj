# cs412NPproj

## Max Clique Problem Presentation -- Sammy Collins
This NP complete problem of finding the max clique in a given graph, essentially means to find the group of nodes, wherein each node of that group is directly connected to every other node in that group. Some applications of this problem include Social Network Analysis, that is, analysis of different groups of friends that could possibly all be target marketed to, DNA analysis, discovering terrorist groups, and more. This problem is important in the field of marketing, computer science, biology, math, and so much more. Cutting this exponential runtime algorithm down can provide advances in DNA sequencing and analysation, target marketing for big coorperations, and an increased efficiency in finding terrorist groups or undiscovered unofficial organizations. According to this paper https://snap.stanford.edu/class/cs224w-readings/tomita06cliques.pdf finding the maximum clique has a worst case runtime of O(3^N/3) for an N-vertex graph.
## Exact Solution - Matt Andrews
## Approximation Code - Hafet Abdulle
## Presentation Slides - Kory Erdmann

Input- Undirected graph, represented as an adjacency list. Vertexes & Edges

N verts  
[Start vertex] [connected vertex] ...
example:\
5\
0 1 2 3\
1 0 2 3\
2 0 1 3\
3 0 1 2\
4 0\

The solution is the subset {0, 1, 2, 3}\
As 0 is connected to 1,2,3 \
1 is connected to 0,2,3\
2 is connected to 0,1,3\
And 3 is connected to 0,1,2\

4 is not included in the answer since it is only connected to 0 and none of the other vertices.


