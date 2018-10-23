## Taken from https://github.com/CianLR/judge-solutions/blob/master/kattis/islandhopping.py
## Tested against kattis:islandhopping, kattis:cats.

import heapq

def complex_dist(a, b):
    import cmath
    return cmath.polar(a - b)[0]

# Takes a list of points of the form complex(x, y).
# Can be modified to take edge weights if the line marked #metric is changed.
# Runs in time proportional to the number of vertices.
def prims(N, points):
    cost = 0
    pq = [(0, 0)]
    in_tree = [False] * N
    tree_dist = [1000000] * N
    tree_size = 0
    while tree_size < N and pq:
        d, u = heapq.heappop(pq)
        if in_tree[u]:
            continue
        in_tree[u] = True
        cost += d
        tree_size += 1
        for v in range(N):
            if u == v or in_tree[v]:
                continue
            dist = complex_dist(points[u], points[v]) #metric
            if dist > tree_dist[v]:
                continue
            tree_dist[v] = dist
            heapq.heappush(pq, (dist, v))
    return cost
