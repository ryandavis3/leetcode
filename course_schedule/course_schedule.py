from typing import Dict, List
from collections import defaultdict


class Graph:
    """
    Directed graph representing course prerequisites.
    """ 
    def __init__(self, numCourses: int, prerequisites: List[List[int]]):
        """
        Constructor for graph.
        """
        self.graph = defaultdict(list)
        for index, prereq in enumerate(prerequisites):
            [end, start] = prereq
            self.graph[start] += [end] 
        self.V = numCourses

    def isCyclicUtil(self, v, visited, recStack):
        """
        Utility for detecting a cycle.
        """
        visited = visited.copy()
        recStack = recStack.copy()
        visited[v] = True
        recStack[v] = True
        for neighbor in self.graph[v]:
            breakpoint()
            if recStack[neighbor] == True:
                return True
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True

    def isCyclic(self):
        """
        Check if there is a cycle in graph.
        """
        visited = [False] * self.V
        recStack = [False] * self.V 
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = Graph(numCourses, prerequisites)
        return not graph.isCyclic


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1,0]]
    graph = Graph(numCourses, prerequisites)  
    result1 = graph.isCyclic()
    print(result1)
    numCourses = 2
    prerequisites = [[1,0], [0,1]]
    graph = Graph(numCourses, prerequisites)
    result2 = graph.isCyclic()
    print(result2)
