from collections import deque


'''
map the string labels to integer indices
get the integer indices for the vertices
add the edge of the adjacency list
 get the integer index for the start vertex
convert the integer indices bACK TO THE STRING LABELS
'''

class Node:

    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Graph:
    def __init__(self):
        self.num_vertices = 0
        self.vertices = {}  # Maps string labels to integer indices
        self.adj_list = []  # Adjacency list represented as a list of lists
    
    def add_vertex(self, label):
        self.vertices[label] = self.num_vertices
        self.adj_list.append([])
        self.num_vertices += 1
    
    def add_edge(self, u, v):
        # Get the integer indices for the vertices
        u_idx = self.vertices[u]
        v_idx = self.vertices[v]
        # Add the edge to the adjacency list
        self.adj_list[u_idx].append(v_idx)
    
    def breadth_first_traversal(self, start_vertex):
        # Get the integer index for the start vertex
        start_idx = self.vertices[start_vertex]
        visited = [False for _ in range(self.num_vertices)]
        queue = [start_idx]
        traversal = []
        
        while queue:
            vertex = queue.pop(0)
            if not visited[vertex]:
                visited[vertex] = True
                traversal.append(vertex)
                for neighbor in self.adj_list[vertex]:
                    queue.append(neighbor)
        
        # Convert the integer indices back to the string labels
        traversal = [list(self.vertices.keys())[list(self.vertices.values()).index(i)] for i in traversal]
        
        return traversal







if __name__ == '__main__':
    # Create a graph
    g = Graph()

    # Add some vertices
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_vertex("G")
    g.add_vertex("H")
    g.add_vertex("I")
    g.add_vertex("K")

    # Add some edges
    g.add_edge("A", "C")
    g.add_edge("A", "E")
    g.add_edge("A", "B")

    g.add_edge("C", "F")
    g.add_edge("B", "D")

    g.add_edge("E", "G")
    g.add_edge("E", "D")
    g.add_edge("E", "F")

    g.add_edge("F", "I")
    g.add_edge("G", "H")
    g.add_edge("F", "H")

    g.add_edge("I", "K")
    g.add_edge("H", "K")

    # Traverse the graph starting from vertex "A"
    traversal = g.breadth_first_traversal("A")

    print(traversal)  # Output: ['A', 'C', 'E', 'B', 'F', 'G', 'D', 'I', 'H', 'K']
