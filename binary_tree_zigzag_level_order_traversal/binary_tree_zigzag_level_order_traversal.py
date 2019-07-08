from typing import List

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

class TreeNode:
    """
    Class for binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Collection:
    """
    Class implementing queue (FIFO) or stack (LIFO).
    """
    def __init__(self, fifo: bool):
        self.values = []
        self.fifo = fifo
    def add(self, value):
        self.values += [value]
    def pop(self):
        if self.fifo:
            return self.values.pop(0)
        return self.values.pop()
    @property
    def is_empty(self):
        return len(self.values) == 0

def zigzag(root: TreeNode) -> List[List[int]]:
    """
    Given a binary tree, return the level order (zigzag) traversal of
    its nodes (from left to right, then right to left for the 
    next level and alternate between).
    """
    # No root given
    if not root:
        return []
    # Root has no children
    if not root.left and not root.right:
        return [[root.val]]
    # Maintain collections for current level and next level
    Qn = Collection(fifo=True)
    Qn.add(root)
    Q = Qn
    array = []
    # Search until no nodes in next level
    fifo = True
    while not Qn.is_empty:
        Qn = Collection(fifo=True)
        level_array = []
        # Visit each node in level in order; add children to
        # collection for next level.
        while not Q.is_empty:
            u = Q.pop()
            level_array += [u.val]
            if u.left:
                Qn.add(u.left)
            if u.right:
                Qn.add(u.right)
        # Reverse level array if necessary, switch direction for next level
        if not fifo:
            level_array = level_array[::-1]
        fifo = not fifo
        array += [level_array]
        Q = Qn
    return array

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        return zigzag(root)
