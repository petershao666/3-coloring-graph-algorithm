import random


class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.size = [1] * n
    def find(self,x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]


def RandGraph(n : int, m : int):

    
    """
    Creates a random undirected graph with n nodes and m edges. The graph is fully connected.
    """

    if n < 1 or not (n - 1 <= m <= n * (n - 1) // 2):
        raise ValueError("Invalid number of nodes or edges")

    all_edges = [(u,v) for u in range(n) for v in range(u+1, n)]

    while True:
        edges = random.sample(all_edges, m)
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        if all(uf.find(v) == uf.find(0) for v in range(n)):
            graph = {i: [] for i in range(n)}

            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            return graph
