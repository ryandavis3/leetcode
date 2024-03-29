import unittest
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_max_money(node: TreeNode, include_head: bool) -> int:
    if include_head and hasattr(node, 'max_value_include'):
        return node.max_value_include
    elif not include_head and hasattr(node, 'max_value_exclude'):
        return node.max_value_exclude
    node_value = node.val if include_head else 0
    if node.left is not None:
        left_value_exclude_next = get_max_money(node=node.left, include_head=False)
        if not include_head:
            left_value_include_next = get_max_money(node=node.left, include_head=True)
            left_value = max(left_value_include_next, left_value_exclude_next) 
        else:
            left_value = left_value_exclude_next
    else:
        left_value = 0
    if node.right is not None:
        right_value_exclude_next = get_max_money(node=node.right, include_head=False)
        if not include_head:
            right_value_include_next = get_max_money(node=node.right, include_head=True)
            right_value = max(right_value_include_next, right_value_exclude_next)
        else:
            right_value = right_value_exclude_next
    else:
        right_value = 0
    max_value = left_value + right_value + node_value
    if include_head:
        node.max_value_include = max_value
    else:
        node.max_value_exclude = max_value
    return max_value
    

def rob(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    max_money_include = get_max_money(node=root, include_head=True)
    max_money_exclude = get_max_money(node=root, include_head=False)
    return max(max_money_include, max_money_exclude)


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return rob(root=root)


#def build_tree_from_root(root: List[int]) -> TreeNode:


class TestRob(unittest.TestCase):
    def test_get_max_money(self) -> None:
        node4 = TreeNode(val=3)
        node5 = TreeNode(val=1)
        node2 = TreeNode(val=2, right=node4)
        node3 = TreeNode(val=3, right=node5)
        node1 = TreeNode(val=3, left=node2, right=node3)
        max_money = get_max_money(node=node1, include_head=True)
        self.assertEqual(max_money, 7)