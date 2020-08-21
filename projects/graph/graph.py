"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # create the new key with the vertex id
        # set the value to an empty set (no edges yet)
        if vertex_id not in self.vertices:
            self.vertices[vertex_id]= set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # find vertex v1 in our vertices, add v2 to the set of edges
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue and enqueue the starting_vertex
        bft_queue = Queue()
        bft_queue.enqueue(starting_vertex)
        # create an empty set to track visited vertices
        visited = set()

        # while queue is not empty
        while bft_queue.size() > 0:
            # get current vertex (dequeue from queue)
            current = bft_queue.dequeue()
            # print(f'Line 50 {current}')
            # check if the current_vertex has not been visited:
            if current not in visited:
                # print current vertex
                print(current)
                # mark current vertex as visited
                # add current vertex to a visited_set
                visited.add(current)
                # queue up all the current vertex's neighbors, so we can visit them next
                for neighbors in self.get_neighbors(current):
                    bft_queue.enqueue(neighbors)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create an empty stack and add the starting_vertex
        dft_stack = Stack()
        dft_stack.push(starting_vertex)
        # create an empty set to track visited vertices
        visited = set()
        # while stack is not empty
        while dft_stack.size() > 0:
            # get current vertex (pop from stack)
            current = dft_stack.pop()
            # check if the current_vertex has not been visited:
            if current not in visited:
                # print current vertex
                print(current)
                # mark current vertex as visited
                # add current vertex to a visited_set
                visited.add(current)
                # push up all the current vertex's neighbors, so we can visit them next
                for neighbors in self.get_neighbors(current):
                    dft_stack.push(neighbors)


    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # set for visited, check every recursion
        if visited is None:
            visited = set()
        # check if start vertex is in visited
        if starting_vertex not in visited:
            # if not in visited print then add to visited
            print(starting_vertex)
            visited.add(starting_vertex)
        # loop through neighbors and if not in visited, recurse with neighbor
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty queue and enqueue the PATH TO starting_vertex
        path = Queue()
        path.enqueue([starting_vertex])
        # create an empty set to track visited vertices
        visited = set()

        # while queue is not empty
        while path.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_path = path.dequeue()
            # set the current vertex to the LAST element of the path
            current_vertex = current_path[- 1]
            print(f' 127 {current_path}')
            # check if the current_vertex has not been visited:
            if current_vertex not in visited:
                # check if current_vertex is destination
                if current_vertex == destination_vertex:
                # if it is, stop and return
                    return current_path
                # mark current vertex as visited
                # add current vertex to a visited_set
                visited.add(current_vertex)

                # queue up new paths with each neighbor:
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    # take current path
                    # append the neighbor to it
                    new_path.append(neighbor)
                    print(f' New path: {new_path}')
                    # queue up new path
                    path.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty queue and enqueue the PATH TO starting_vertex
        path = Stack()
        path.push([starting_vertex])
        # create an empty set to track visited vertices
        visited = set()

        # while queue is not empty
        while path.size() > 0:
            # get current vertex PATH (dequeue from queue)
            current_path = path.pop()
            # set the current vertex to the LAST element of the path
            current_vertex = current_path[- 1]
            print(f' 127 {current_path}')
            # check if the current_vertex has not been visited:
            if current_vertex not in visited:
                # check if current_vertex is destination
                if current_vertex == destination_vertex:
                # if it is, stop and return
                    return current_path
                # mark current vertex as visited
                # add current vertex to a visited_set
                visited.add(current_vertex)

                # queue up new paths with each neighbor:
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = list(current_path)
                    # take current path
                    # append the neighbor to it
                    new_path.append(neighbor)
                    print(f' New path: {new_path}')
                    # queue up new path
                    path.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # define path variable to return when complete
        if path is None:
            path = [starting_vertex]
        # keep track of visited options
        if visited is None:
            visited = set()
        #check if current vertex in visited
        if path[-1] not in visited:
            #if not in visited, add to visited
            if path[-1] == destination_vertex:
                return path
            visited.add(path[-1])
        # check through neighbors, add to path?
            for neighbor in self.get_neighbors(path[-1]):
                new_path = list(path)
                new_path.append(neighbor)
                recurse = self.dfs_recursive(starting_vertex, destination_vertex, visited, new_path)
                if recurse:
                    return recurse
                
        

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    # print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
