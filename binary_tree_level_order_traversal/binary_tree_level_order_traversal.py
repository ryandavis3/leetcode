from typing import List

# https://leetcode.com/problems/binary-tree-level-order-traversal/

class TreeNode:
    """
    Class for binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Queue:
    """
    Class implementing queue (FIFO).
    """
    def __init__(self):
        self.Q = []
    def enqueue(self, value):
        self.Q = self.Q + [value]
    def dequeue(self):
        value = self.Q[0]
        self.Q = self.Q[1:]
        return value
    @property
    def is_empty(self):
        return len(self.Q) == 0

def levelOrder(root: TreeNode) -> List[List[int]]:
    """
    Given a binary tree, return the level order traversal of 
    its nodes.
    """
    # No root given
    if not root:
        return []
    # Root has no children
    if not root.left and not root.right:
        return [[root.val]]
    # Maintain queues for current level and next level
    Qn = Queue()
    Qn.enqueue(root)
    Q = Qn
    array = []
    # Search until no nodes in next level
    while not Qn.is_empty:
        Qn = Queue()
        level_array = []
        # Visit each node in level in order; add children to
        # queue for next level.
        while not Q.is_empty:
            u = Q.dequeue()
            level_array += [u.val]
            if u.left:
                Qn.enqueue(u.left)
            if u.right:
                Qn.enqueue(u.right)
        array += [level_array]
        Q = Qn
    return array 

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
       return levelOrder(root) 
