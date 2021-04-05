class PriorityQueue:
    def __init__(self, a: int, b: int, c: int):
        # Sort values
        self.L = [("a", a), ("b", b), ("c", c)]
        self.L = sorted(L, key = lambda x: x[1], reverse=True)
    def pop() -> str:
        s = self.L[0]
        self.L[0] -= 1
    def continue(self) -> bool:
        for i in range(3):
            if self.L[i][1] == 0:
                return False
        return True

def longestDiverseString(self, a: int, b: int, c: int) -> str:
    pq = PriorityQueue(a, b, c)
    s = ""
    

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pass

if __name__ == '__main__':

