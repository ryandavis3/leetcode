# https://leetcode.com/problems/binary-tree-maximum-path-sum/

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
    if node.left or node.right:
        return False
    return True

def maxPathSum(root: TreeNode) -> int:
    """
    Find maximum path sum through binary tree. A path is defined
    as any sequence of nodes from some starting node to any 
    node in the tree along the parent-child connections. The path 
    must contain at least one node and does not need to go through
    the root.
    """
    # No node passed!
    if not root:
        max_add_sum = 0
        max_sum = -10**10
        return [max_sum, max_add_sum]
    # Node is leaf
    if isLeaf(root):
        max_add_sum = root.val
        max_sum = root.val
        return [max_sum, max_add_sum]
    # Node has at least one child
    [left_sum, left_add] = maxPathSum(root.left)
    [right_sum, right_add] = maxPathSum(root.right)
    # Max sums for including and excluding node
    max_sum_include = max(left_add, 0) + max(right_add, 0) + root.val
    max_sum_exclude = max(left_sum, right_sum, root.val)
    max_sum = max(max_sum_include, max_sum_exclude)
    # Max addable sum contains root and at most one of left 
    # and right children.
    max_add_sum = root.val + max(left_add, right_add, 0)
    return [max_sum, max_add_sum]

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        [max_sum, max_add_sum] = maxPathSum(root)
        return max_sum
