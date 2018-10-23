## Taken from https://github.com/INSAlgo/ICPC-Notebook/blob/master/python/graphs/mergefind_and_kruskal.py
## Tested against kattis:minspantree

# Kruskal's algorithm for minimum spanning tree.
# Includes Union-Find.
parent = {}
rank = {}

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex_a, vertex_b):
    root_a = find(vertex_a)
    root_b = find(vertex_b)
    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
    if rank[root_a] == rank[root_b]:
        rank[root_b] += 1

# Takes an object with the following structure:
# {
#   'edges': [0, 1, 2, 3, ..],
#   'vertices': [(w0, u0, v0), (w1, u1, v1), ...],
# }
# Where w0 = weight of edge from u0 to v0.
def kruskal(graph):
    mst = set()
    edges = list(graph['edges'])
    edges.sort()
    for vertex in graph['vertices']:
        make_set(vertex)
    for edge in edges:
        weight, vertex_a, vertex_b = edge
        if find(vertex_a) != find(vertex_b):
            union(vertex_a, vertex_b)
            mst.add(edge)
    return sorted(mst)
