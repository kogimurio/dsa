# Implementation of Dijkstra's Algorithm on Undirected Graphs
# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#     def add_edge(self, u, v, weight):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = weight
#             self.adj_matrix[v][u] = weight
#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#     def dijkstra(self, start_vertex_data):
#         start_vertex = self.vertex_data.index(start_vertex_data)
#         distance = [float('inf')] * self.size
#         distance[start_vertex] = 0
#         visited = [False] * self.size
        
#         # Process Vertices One by One
#         for _ in range(self.size):
#             min_distance = float('inf')
#             u = None
#             # Find the Closest Unvisited Vertex
#             for i in range(self.size):
#                 if not visited[i] and distance[i] < min_distance:
#                     min_distance = distance[i]
#                     u = i
#             if u is None:
#                 break
#             visited[u] = True
            
#             # Update Neighbor Distances
#             for v in range(self.size):
#                 if self.adj_matrix[u][v] != 0 and not visited[v]:
#                     alt = distance[u] + self.adj_matrix[u][v]
#                     if alt < distance[v]:
#                         distance[v] = alt
#         return distance
# g = Graph(7)

# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0, 4)  # D - A, weight 5
# g.add_edge(3, 4, 2)  # D - E, weight 2
# g.add_edge(0, 2, 3)  # A - C, weight 3
# g.add_edge(0, 4, 4)  # A - E, weight 4
# g.add_edge(4, 2, 4)  # E - C, weight 4
# g.add_edge(4, 6, 5)  # E - G, weight 5
# g.add_edge(2, 5, 5)  # C - F, weight 5
# g.add_edge(2, 1, 2)  # C - B, weight 2
# g.add_edge(1, 5, 2)  # B - F, weight 2
# g.add_edge(6, 5, 5)  # G - F, weight 5

# # Dijkstra's algorithm from D to all vertices
# print("\nDijkstra's Algorithm starting from vertex D")
# distances = g.dijkstra('D')
# for i, d in enumerate(distances):
#     print(f"Distanc from D to {g.vertex_data[i]}: {d}")
   
# Implementation of Dijkstra's Algorithm on Directed Graphs 

# class Graph:
#     def __init__(self, size):
#         self.adj_matrix = [[0] * size for _ in range(size)]
#         self.size = size
#         self.vertex_data = [''] * size
#     def add_edge(self, u, v, weight):
#         if 0 <= u < self.size and 0 <= v < self.size:
#             self.adj_matrix[u][v] = weight 
#     def add_vertex_data(self, vertex, data):
#         if 0 <= vertex < self.size:
#             self.vertex_data[vertex] = data
#     def dijkstra(self, start_vertex_data):
#         start_vertex = self.vertex_data.index(start_vertex_data)
#         distances = [float('inf')] * self.size
#         distances[start_vertex] = 0
#         visited = [False] * self.size
#         predecessors = [None] * self.size
        
#         for _ in range(self.size):
#             min_distance = float('inf')
#             u = None
#             for i in range(self.size):
#                 if not visited[i] and distances[i] < min_distance:
#                     min_distance = distances[i]
#                     u = i
#             if u is None:
#                 break
#             visited[u] = True
            
#             for v in range(self.size):
#                 if self.adj_matrix[u][v] != 0 and not visited[v]:
#                     alt = distances[u] + self.adj_matrix[u][v]
#                     if alt < distances[v]:
#                         distances[v] = alt
#                         predecessors[v] = u
#         return distances, predecessors
#     def get_path(self, predecessors, start_vertex, end_vertex):
#         path = []
#         current = self.vertex_data.index(end_vertex)
#         while current is not None:
#             path.insert(0, self.vertex_data[current])
#             current = predecessors[current]
#             if current == self.vertex_data.index(start_vertex):
#                 path.insert(0, start_vertex)
#                 break
#         return '->'.join(path) # Join the vertics with '->'
    
# g = Graph(7)

# g.add_vertex_data(0, 'A')
# g.add_vertex_data(1, 'B')
# g.add_vertex_data(2, 'C')
# g.add_vertex_data(3, 'D')
# g.add_vertex_data(4, 'E')
# g.add_vertex_data(5, 'F')
# g.add_vertex_data(6, 'G')

# g.add_edge(3, 0, 4)  # D -> A, weight 5
# g.add_edge(3, 4, 2)  # D -> E, weight 2
# g.add_edge(0, 2, 3)  # A -> C, weight 3
# g.add_edge(0, 4, 4)  # A -> E, weight 4
# g.add_edge(4, 2, 4)  # E -> C, weight 4
# g.add_edge(4, 6, 5)  # E -> G, weight 5
# g.add_edge(2, 5, 5)  # C -> F, weight 5
# g.add_edge(1, 2, 2)  # B -> C, weight 2
# g.add_edge(1, 5, 2)  # B -> F, weight 2
# g.add_edge(6, 5, 5)  # G -> F, weight 5

# # Dijkstra's algorithm from D to all vertices
# print("Dijkstra's Algorithm starting from vertex D:\n")
# distances, predecessors = g.dijkstra('D')
# for i, d in enumerate(distances):
#     path = g.get_path(predecessors, 'D', g.vertex_data[i])
#     print(f"{path}, Distance: {d}")
    
# Dijkstra's algorithm implemented to find the shortest path to a single destination vertex
class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size
    def add_edge(self, u, v, weight):
        if 0 <= u < self.size and 0 <= v < self.size:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
    def add_vertex_data(self, vertex, data):
        if 0 <= vertex < self.size:
            self.vertex_data[vertex] = data
           
    def dijkstra(self, start_vertex_data, end_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        end_vertex = self.vertex_data.index(end_vertex_data)
        distances = [float('inf')] * self.size
        predecessors = [None] * self.size
        distances[start_vertex] = 0
        visited = [False] * self.size
        
        for _ in range(self.size):
            min_distance = float('inf')
            u = None
            for i in range(self.size):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i
            if u is None or u == end_vertex:
                print(f"Breaking out of loop. Current vertex: {self.vertex_data[u]}")
                print(f"Distances: {distances}")
                break
            visited[u] = True
            print(f"Visisted vertex: {self.vertex_data[u]}")
            
            for v in range(self.size):
                if self.adj_matrix[u][v] != 0 and not visited[v]:
                    alt = distances[u] + self.adj_matrix[u][v]
                    if alt < distances[v]:
                        distances[v] = alt
                        predecessors[v] = u
        return distances[end_vertex], self.get_path(predecessors, start_vertex_data, end_vertex_data)
    def get_path(self, predecessor, start_vertex, end_vertex):
        path = []
        current = self.vertex_data.index(end_vertex)
        while current is not None:
            path.insert(0, self.vertex_data[current])
            current = predecessor[current]
            if current == self.vertex_data.index(start_vertex):
                path.insert(0, start_vertex)
                break
        return '->'.join(path)

g = Graph(10)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')
g.add_vertex_data(7, 'H')
g.add_vertex_data(8, 'I')
g.add_vertex_data(9, 'J')

g.add_edge(3, 0, 4)  # D - A, weight 5
g.add_edge(3, 4, 2)  # D - E, weight 2
g.add_edge(0, 2, 3)  # A - C, weight 3
g.add_edge(0, 4, 4)  # A - E, weight 4
g.add_edge(4, 2, 4)  # E - C, weight 4
g.add_edge(4, 6, 5)  # E - G, weight 5
g.add_edge(2, 5, 5)  # C - F, weight 5
g.add_edge(2, 1, 2)  # C - B, weight 2
g.add_edge(1, 5, 2)  # B - F, weight 2
g.add_edge(6, 5, 5)  # G - F, weight 5
g.add_edge(6, 8, 4)  # G - I, weight 4
g.add_edge(6, 7, 5)  # G - H, weight 5
g.add_edge(8, 9, 2)  # I - J, weight 2

print("Dijkstra's Algorithm, from vertex D to F:\n")
distance, path = g.dijkstra('D','F')
print(f"Path: {path}, Distance: {distance}")
        
                    
           