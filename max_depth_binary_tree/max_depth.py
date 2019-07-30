class TreeNode:
    """
    Node in binary tree.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Queue:
    """
    Class for FIFO queue.
    """
    def __init__(self):
        self.Q = []
    def enqueue(self, x: int):
        self.Q = [x] + self.Q
    def dequeue(self) -> int:
        return self.Q.pop()
    @property
    def is_empty(self):
        return len(self.Q) == 0

def maxDepth(root: TreeNode):
    """
    Run breadth-first search on binary tree and get max
    depth.
    """
    if not root:
        return 0
    max_depth = 0
    # Previous level
    prev = Queue()
    prev.enqueue(root)
    while not prev.is_empty:
        # Increment depth
        max_depth += 1
        level = Queue()
        # Add nodes in next level to queue
        while not prev.is_empty:
            u = prev.dequeue()
            if u.left:
                level.enqueue(u.left)
            if u.right:
                level.enqueue(u.right)
        # Update previous level
        prev = level
    return max_depth

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return maxDepth(root)        
