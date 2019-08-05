from typing import List

# https://leetcode.com/problems/path-sum-ii/

class TreeNode:
    """
    Binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isLeaf(node: TreeNode) -> bool:
    """
    Return True if node is leaf, else return False.
    """
    if not node.left and not node.right:
        return True
    return False

def addToPaths(paths: List, val: int):
    """
    Add value to each path in list.
    """
    return [[val] + path for path in paths]

def updatePaths(paths: List, paths_new: List, val: int):
    """
    Update paths with new value
    """
    if paths_new is not None:
        paths_new = addToPaths(paths_new, val) 
        paths += paths_new
    return paths

def pathSum(root: TreeNode, val: int) -> bool:
    """
    Find all root-to-leaf paths in a binary tree where
    each path's sum equals the given sum.
    """
    # No node given
    if not root:
        return None
    # If node value match and node is leaf, found path
    if root.val == val and isLeaf(root):
        return [[root.val]]
    # Check left and right subtrees
    paths = []
    sub_val = val - root.val
    left = pathSum(root.left, sub_val)
    paths = updatePaths(paths, left, root.val)
    right = pathSum(root.right, sub_val)
    paths = updatePaths(paths, right, root.val)
    if not paths:
        return None
    return paths 


class Solution:
    def pathSum(self, root: TreeNode, val: int) -> bool:
        return pathSum(root, val)
