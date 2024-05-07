
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = []
        mst_cost = 0

        # Start Prim's algorithm from vertex 0
        heapq.heappush(min_heap, (0, 0))  # (weight, vertex)
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if not visited[u]:
                mst_cost += weight
                visited[u] = True
                for v, w in self.graph[u]:
                    if not visited[v]:
                        heapq.heappush(min_heap, (w, v))

        return mst_cost

# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

print("Minimum Spanning Tree cost:", g.prim_mst())
