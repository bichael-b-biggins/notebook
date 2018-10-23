## Taken from https://github.com/INSAlgo/ICPC-Notebook/blob/master/python/graphs/mergefind_and_kruskal.py
# TODO: Read over it, some parts don't look 100% right.

# Kruskal's algorithm for minimum spanning tree.
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

def kruskal(graph):
    for vertex in graph['vertices']:
        make_set(vertex)
        mst = set()
        edges = list(graph['edges'])
        edges.sort()
        for edge in edges:
            weight, vertex_a, vertex_b = edge
            if find(vertex_a) != find(vertex_b):
                union(vertex_a, vertex_b)
                mst.add(edge)
        return sorted(mst)
