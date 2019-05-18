# Solve as connected components problem

from typing import List

class Node():
    """
    Class representing node in graph.
    """
    def __init__(self, value: int):
        """
        Initialize node with value.
        """
        self.value = value
        self.adjacent = list()
        self.visited = False
    def add_adjacent(self, node):
        """
        Specify adjacent node.
        """
        if node not in self.adjacent:
            self.adjacent.append(node)
    def __eq__(self, other):
        return self.value == other

def buildGraph(M: List[List[int]]) -> List:
    """
    Build graph from adjacency matrix.
    """
    l = len(M)
    G = [Node(i) for i in range(l)]
    for i in range(len(M)):
        for j in range(len(M)):
            if M[i][j]:
                G[i].add_adjacent(G[j])
    return G

def DFS(G: List, i: int, U: List) -> List:
    """
    Depth-first search.
        * G is the graph
        * i is the index of the node to visit
        * U is a list of un-visited nodes 
    """
    node = G[i]
    node.visited = True
    U.remove(i)
    for adj_node in node.adjacent:
        if not adj_node.visited:
            DFS(G, adj_node.value, U)
    return [G, U]

def findComponents(M: List[List[int]]) -> int:
    """
    Find number of connected components.
    """
    G = buildGraph(M)
    U = list(range(len(M)))
    n_components = 0
    while U:
        n_components += 1
        [G, U] = DFS(G, U[0], U)
    return n_components

