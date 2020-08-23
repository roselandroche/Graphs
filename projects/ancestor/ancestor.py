
def earliest_ancestor(ancestors, starting_node):
    pass

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
Suggested to use DFT, but that is random... how to make sure it returns the longest path?
Could do BFT, would ensure that the last path found would be longest...
Graph is uni-directional, because it's a parent child relationship
    Have to search from the top down
    
P

'''