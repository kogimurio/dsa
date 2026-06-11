from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u].append(v)
    def add_edge_undirected(self, u, v):
        self.add_edge(u, v)
        self.add_edge(v, u)
    def traverse(self):
        for vertex in self.graph:
            print(vertex, " -> ", self.graph[vertex])
    def search(self, u, v):
        if u in self.graph and v in self.graph[u]:
            return True
        return False
    def delete_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
    def delete_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
        for v in self.graph:
            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)
    def dfs(self, start):
        visited = set()
        
        def dfs_helper(vertex):
            if vertex in visited:
                return
            
            print(vertex, end=" -> ")
            visited.add(vertex)
            
            for neighbor in self.graph[vertex]:
                dfs_helper(neighbor)
        dfs_helper(start)
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            vertex = queue.popleft()
            print(vertex, end=" - > ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
g = Graph()

# Insert
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "E")


g.traverse()
print()

# DFS
g.dfs("A")
print()
# BFS
g.bfs("A")




        