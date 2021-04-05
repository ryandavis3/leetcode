class PriorityQueue:

    def __init__(self, a: int, b: int, c: int):
        """
        Constructor.
        """
        # Sort values
        self.L = [["a", a], ["b", b], ["c", c]]
        self.L = sorted(self.L, key = lambda x: x[1], reverse=True)
        self.consecutive = 0
        self.string = ""

    def pop(self, index: int=0) -> str:
        """
        Pop 'top' element from the queue.
        """
        s = self.L[index][0]
        self.L[index][1] -= 1
        self.L = sorted(self.L, key = lambda x: x[1], reverse=True)
        return s
    
    def go(self) -> bool:
        """
        Return True if we can continue, else return False.
        """
        skip = None
        if self.consecutive == 2:
            skip = self.string[-1]
        for i in range(3):
            if self.L[i][0] == skip:
                continue
            if self.L[i][1] > 0:
                return True
        return False

    def add(self):
        skip = None
        if self.consecutive == 2:
            skip = self.string[-1]
            self.consecutive = 0
        else:
            self.consecutive += 1
        if self.L[0][0] == skip:    
            self.string += self.pop(index=1)
        else:
            self.string += self.pop(index=0)

def longestDiverseString(a: int, b: int, c: int) -> str:
    """
    Get longest 'diverse' string satisfying requirements.
    """
    pq = PriorityQueue(a, b, c)
    while pq.go():
        pq.add()
    return pq.string


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        return longestDiverseString(a, b, c)


if __name__ == '__main__':
    a = 1 
    b = 3
    c = 5
    s = longestDiverseString(a, b, c)
    print(s)
