from typing import List
from math import log, ceil

# Utilities for binary trees

class TreeNode:
    """
    Class for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def popArray(array: List[int]) -> int:
    """
    Pop value from front of array. Return None if array
    is None.
    """
    if array:
        val = array.pop(0)
    else:
        val = None
    return val

def createNode(val: int) -> TreeNode:
    """
    Create node from value. If value is None, return None.
    """
    if val is None:
        node = None
    else:
        node = TreeNode(val)
    return node

def arrayToTree(array: List[int]) -> TreeNode:
    """
    Convert array of integers to binary tree.
    """
    # Root of tree
    root = TreeNode(array[0])
    L = len(array)
    height = int(ceil(log(L+1, 2)))
    level = 1
    nodes_prev = [root]
    array = array[1:]
    # Build one level at a time
    while level < height:
        nodes_level = []
        for node_prev in nodes_prev:
            # Node is None - move to next node
            if node_prev is None:
                array = array[2:]
                continue
            # Left child
            val_left = popArray(array)
            node = createNode(val_left)
            node_prev.left = node
            nodes_level += [node]
            # Right child
            val_right = popArray(array)
            node = createNode(val_right)
            node_prev.right = node
            nodes_level += [node]
        # Update nodes on previous level
        nodes_prev = nodes_level
        level += 1
    return root

class Queue:
    """
    Class implementing queue (LIFO).
    """
    def __init__(self):
        self.Q = []
        # L is the number of non-None elements in queue
        self.L = 0
    def enqueue(self, value):
        self.Q = self.Q + [value]
        if value is not None:
            self.L += 1
    def dequeue(self):
        value = self.Q[0]
        if value is not None:
            self.L -= 1
        self.Q = self.Q[1:]
        return value
    @property
    def is_empty(self):
        return self.L == 0

def padArrayNone(array: List[int]):
    """
    Pad array with None values.
    """
    L = len(array)
    height = int(ceil(log(L+1, 2)))
    n = 2 ** height - 1
    array += [None] * (n - L)

def treeToArray(root: TreeNode) -> List[int]:
    """
    Convert binary tree to array. Represent missing node as None.
    Use breadth-first search.
    """
    Q = Queue()
    Q.enqueue(root)
    array = []
    while not Q.is_empty:
        u = Q.dequeue()
        if u is None:
            array += [None]
            Q.enqueue(None)
            Q.enqueue(None)
        else:
            array += [u.val]
            Q.enqueue(u.left)
            Q.enqueue(u.right)
    padArrayNone(array)
    return array
