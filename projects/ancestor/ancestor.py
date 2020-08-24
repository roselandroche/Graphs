class Graph():
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, new_vertex):
        if new_vertex not in self.vertices:
            self.vertices[new_vertex] = set()
    
    def add_edge(self, vertex_1, vertex_2):
        self.vertices[vertex_1].add(vertex_2)

    def get_neighbors(self, vertex):
        return self.vertices[vertex]

    def dft(self, start_vertex, visited=None, path=None, result=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
        if result is None:
            result = []
        
        path = path + [start_vertex]

        #if start is at top, return -1
        if len(self.get_neighbors(start_vertex)) == 0 and len(visited) == 0:
            return -1
        #else if get neighbor on start == 0
        elif len(self.get_neighbors(start_vertex)) == 0:
            #append result via tuple (start, len_path)
            result.append((start_vertex, len(path)))
        #loop over neighbors
        for neighbor in self.get_neighbors(start_vertex):
            #add start to visited
            visited.add(start_vertex)
            #recurse on parent
            self.dft(neighbor, visited, path, result)
        return result

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for ancestor in ancestors:
        v1, v2 = ancestor
        graph.add_vertex(v1)
        graph.add_vertex(v2)
        graph.add_edge(v2, v1)
    result = graph.dft(starting_node)
    # iterate through result tuples
    # if it's not a tuple
    # return value
    # find tuple with highest value at index 1
    # return index 0 of same tuple
    # if more than one have same value at index 1
    # return tuple with lowest value at index 0
    if result == -1:
        return result
    new_tuple = (0,0)
    for data in result:
        ancestor, length = data
        if length > new_tuple[1]:
            new_tuple = (ancestor, length)
        elif length == new_tuple[1]:
            if ancestor < new_tuple[0]:
                new_tuple = (ancestor, length)
    return new_tuple[0]

'''
U
Input
    List of (parent, child) pairs
    Each individual is unique

Output
    Return the individual furthest away from the input individual
    If more than one at that level of distance:
        Return the individual with lowest numeric id
    If input individual has no parents:
        Return -1

Have to traverse from starting_node to end of all ancestors and return the longest possible path's end
    (but backwards)
Use DFS - 
Graph is uni-directional, because it's a parent child relationship
    Have to search from the top down

P

'''

ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(ancestors, 1))
print(earliest_ancestor(ancestors, 2))
print(earliest_ancestor(ancestors, 3))
print(earliest_ancestor(ancestors, 4))
print(earliest_ancestor(ancestors, 5))
print(earliest_ancestor(ancestors, 6))
print(earliest_ancestor(ancestors, 7))
print(earliest_ancestor(ancestors, 8))
print(earliest_ancestor(ancestors, 9))
print(earliest_ancestor(ancestors, 10))
print(earliest_ancestor(ancestors, 11))