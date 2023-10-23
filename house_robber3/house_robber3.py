import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_max_money(node: TreeNode, include_head: bool) -> int:
    node_value = node.val if include_head else 0
    if node.left is None and node.right is None:
        return node_value
    if node.left is None and node.right is not None:
        value = node_value + get_max_money(node=node.right, include_head=False)
        return value
    if node.left is not None and node.right is None:
        value = node_value + get_max_money(node=node.left, include_head=False)
        return value


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return get_max_money(node=root, include_head=True)


#def build_tree_from_root(root: List[int]) -> TreeNode:


class TestRob(unittest.TestCase):
    pass