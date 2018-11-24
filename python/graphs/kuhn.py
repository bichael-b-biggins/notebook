
def dfs(adj, visited, right, left, u):
    visited[u] = True
    for v in adj[u]:
        # If the adj node unpaired then pair it to this.
        # Otherwise try and pair the adj one's pair to somewhere else.
        if (left[v] == -1 or
            (not visited[left[v]] and
             dfs(adj, visited, right, left, left[v]))):
            left[v] = u
            right[u] = v
            return True
    return False


def kuhn(N, M, adj):
    right_pair = [-1] * N
    left_pair = [-1] * M
    visited = [False] * N
    for i in xrange(N):
        if right_pair[i] != -1:
            continue  # Already paired
        visited = [False] * N
        # If false then this node can't be paired.
        dfs(adj, visited, right_pair, left_pair, i)
    return left_pair    

