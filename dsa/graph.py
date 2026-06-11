vertexData = ['A', 'B', 'C', 'D']

adjacency_matrix = [
    [0, 1, 1, 1], #Edges for A
    [1, 0, 1, 0], #Edges for B
    [1, 1, 0, 0], #Edges for C
    [1, 0, 0, 0], #Edges for D
]

def print_adjacency_matrix(matrix):
    print("\nAdjancency Matrix")
    for row in matrix:
        print(row)

def print_connections(matrix, vertices):
    print("\nConnections for each verticx")
    for i in range(len(vertices)):
        print(f"{vertices[i]}: ", end="")
        for j in range(len(vertices)):
            if matrix[i][j]:
                print(vertices[j], end=" ")
        print()
# print_adjacency_matrix(adjacency_matrix)
# print_connections(adjacency_matrix, vertexData)

# Implementing of an Undirected Graph and its adjacency matrix using classes

class Graph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex data")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1) # A - B
g.add_edge(0, 2) # A - C
g.add_edge(0, 3) # A - D
g.add_edge(1, 2) # B - C

# g.print_graph()


# Implimentation of A directed and weighted Graph,and its adjacency matrix using classes
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[None] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacecy Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(lambda x: str(x) if x is not None else '0', row)))
        print('\nVertex Data')
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
g = Graph(4)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_edge(0, 1, 3) # A - > B with weight 3
g.add_edge(0, 2, 2) # A - > C with weight 2
g.add_edge(3, 0, 4) # D - > A with weight 4
g.add_edge(2, 1, 1) # C - > B with weight 1

# g.print_graph()

# Implimenting Depth First Search Traversal  for undirected graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u and u < self.size and 0 <= v and v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex Data")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=" ")
        
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)
    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0) # D - > A
g.add_edge(0, 2) # A - > C
g.add_edge(0, 3) # A - > D
g.add_edge(0, 4) # A - > E
g.add_edge(4, 2) # E - > C
g.add_edge(2, 5) # C - > F
g.add_edge(2, 1) # C - > B
g.add_edge(2, 6) # C - > G
g.add_edge(1, 5) # B - > F

# g.print_graph()

# print("\nDepth First Search starting from vertex D:")
# g.dfs('D')

# Implimenting Breadth First Search Traversal for undirected graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
            self.adj_matrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("\nAdjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nVertex: Data")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex: {vertex}, {data}")
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=" ")
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            
g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0) # D - > A
g.add_edge(0, 2) # A - > C
g.add_edge(0, 3) # A - > D
g.add_edge(0, 4) # A - > E
g.add_edge(4, 2) # E - > C
g.add_edge(2, 5) # C - > F
g.add_edge(2, 1) # C - > B
g.add_edge(2, 6) # C - > G
g.add_edge(1, 5) # B - > F

# g.print_graph()

# print("\nBreadth First Search starting from vertex D:")
# g.bfs('D')

# Implimenting Depth and Breadth First Search Traversal for directed graph
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))
        print("\nvertex Data")
        for vertex, data in enumerate(self.vertex_data):
            print(f"Vertex: {vertex} {data}")
    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')
        
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)
    def dfs(self, start_vertex_data):
        visited = [False] * self.size
        
        start_vertex = self.vertex_data.index(start_vertex_data)
        self.dfs_util(start_vertex, visited)
    def bfs(self, start_vertex_data):
        queue = [self.vertex_data.index(start_vertex_data)]
        visited = [False] * self.size
        visited[queue[0]] = True
        
        while queue:
            current_vertex = queue.pop(0)
            print(self.vertex_data[current_vertex], end=' ')
            
            for i in range(self.size):
                if self.adj_matrix[current_vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True
            
g = Graph(7)
g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0) # D - > A
g.add_edge(0, 2) # A - > C
g.add_edge(0, 3) # A - > D
g.add_edge(0, 4) # A - > E
g.add_edge(4, 2) # E - > C
g.add_edge(2, 5) # C - > F
g.add_edge(2, 1) # C - > B
g.add_edge(2, 6) # C - > G
g.add_edge(1, 5) # B - > F

# g.print_graph()

# print("\nBreadth First Search starting from vertex D:")
# g.bfs('D')
# print("\ndeapth First Search starting from vertex D:")
# g.dfs('D')

# DFS Cycle Detection for Undirected Graphs
# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#     def add_edge(self, u, v):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = 1
#             self.adj_matrix[v][u] = 1
#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#     def print_graph(self):
#         print("\nAdjacency Matrix:")
#         for row in adjacency_matrix:
#             print(' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, index in enumerate(self.vertex_data):
#             print(f"Vertex {vertex}: {index}")
#     def dfs_util(self, v, visited, parent):
#         visited[v] = True
        
#         for i in range(self.size):
#             if self.adj_matrix[v][i] == 1:
#                 if not visited[i]:
#                     if self.dfs_util(i, visited, v):
#                         return True
#                 elif parent != i:
#                     return True
#         return False
#     def is_cyclic(self):
#         visited = [False] * self.size
#         for i in range(self.size):
#             if not visited[i]:
#                 if self.dfs_util(i, visited, -1):
#                     return True
#         return False
# g = Graph(7)
# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0)  # D - A   
# g.add_edge(0, 2)  # A - C 
# g.add_edge(0, 3)  # A - D 
# g.add_edge(0, 4)  # A - E 
# g.add_edge(4, 2)  # E - C 
# g.add_edge(2, 5)  # C - F 
# g.add_edge(2, 1)  # C - B 
# g.add_edge(2, 6)  # C - G
# g.add_edge(1, 5)  # B - F  

# g.print_graph()

# print("\nGraph has cycle:", g.is_cyclic())         

# DFS Cycle Detection for Directed Graphs
# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#     def add_edge(self, u, v):
#         if 0 <= u < self.size and 0 <= 0 < self.size:
#             self.adj_matrix[u][v] = 1
#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#     def print_graph(self):
#         print("Print Matrix:")
#         for row in self.adj_matrix:
#             print(' '.join(map(str, row)))
#         print("\nVertex Data:")
#         for vertex, index in enumerate(self.vertex_data):
#             print(f"Vertex {vertex} {index}")  
#     def dfs_util(self, v, visited, recStack):
#         visited[v] = True
#         recStack[v] = True
#         print("Current vertex:", self.vertex_data[v])
        
#         for i in range(self.size):
#             if self.adj_matrix[v][i] == 1:
#                 if not visited[i]:
#                     if self.dfs_util(i, visited, recStack):
#                         return True
#                 elif recStack[i]:
#                     return True
#         recStack[v] = False
#         return False
#     def is_cyclic(self):
#         visited = [False] * self.size
#         recStack = [False] * self.size
#         for i in range(self.size):
#             if not visited[i]:
#                 print()
#                 if self.dfs_util(i, visited, recStack):
#                     return True
#         return False
# g = Graph(7)

# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0)  # D -> A
# g.add_edge(0, 2)  # A -> C
# g.add_edge(2, 1)  # C -> B
# g.add_edge(2, 4)  # C -> E
# g.add_edge(1, 5)  # B -> F
# g.add_edge(4, 0)  # E -> A
# g.add_edge(2, 6)  # C -> G

# g.print_graph()

# print("Graph has cycle:", g.is_cyclic())
                     
# Detecting cycles using Union-Find
class Graph:
    def __init__(self, size):
        self.adj_mtrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
        self.parent = [i for i in range(size)] # Union-Find array
    def add_edge(self, u, v): 
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_mtrix[u][v] = 1
            self.adj_mtrix[v][u] = 1
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        print('Union:', self.vertex_data[x],'+',self.vertex_data[y])
        self.parent[x_root] = y_root
        print(self.parent, '\n')
    def is_cyclic(self):
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if self.adj_mtrix[i][j]:
                    x = self.find(i)
                    y = self.find(j)
                    if x == y:
                        return True
                    self.union(x, y)
        return False
g = Graph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(1, 0)  # B - A
g.add_edge(0, 3)  # A - D
g.add_edge(0, 2)  # A - C
g.add_edge(2, 3)  # C - D
g.add_edge(3, 4)  # D - E
g.add_edge(3, 5)  # D - F
g.add_edge(3, 6)  # D - G
g.add_edge(4, 5)  # E - F

print("Graph has cycle:", g.is_cyclic())


