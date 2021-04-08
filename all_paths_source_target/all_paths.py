from typing import Dict, List

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    
    # Target node to hit
    N = len(graph)
    
    # Memoize for speed
    memo: Dict = {}

    # Backtrack for solution
    def backtrack(i: int) -> List[List[int]]:
        # Found memoized solution
        if i in memo:
            return memo[i]
        # Reached the end!
        if i == N - 1:
            return [[i]]
        options = []
        # Explore each edge
        edges = graph[i]
        for edge in edges:
            options += backtrack(edge)
        # No path to target
        if len(options) == 0:
            return []
        # Explore paths
        paths = []
        for option in options:
            if len(option) > 0:
                concat = [i] + option
                paths += [concat]
        memo[i] = paths
        return paths
    
    return backtrack(0)


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        return allPathsSourceTarget(graph)


if __name__ == "__main__":
    graph = [[1,2],[3],[3],[]]
    result = allPathsSourceTarget(graph)
    print(result)
    graph = [[4,3,1],[3,2,4],[3],[4],[]]
    result1 = allPathsSourceTarget(graph)
    print(result1)
