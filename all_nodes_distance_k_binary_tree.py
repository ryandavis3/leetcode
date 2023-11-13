from typing import Dict, List
from unittest import TestCase


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_path_to_target(root: TreeNode, target: TreeNode) -> List[int]:
    if root.val == target.val:
        return [root.val]



class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        pass


class TestDistanceK(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.root = TreeNode(x=1)
        cls.node2 = TreeNode(x=2)
        cls.node3 = TreeNode(x=3)
        cls.node4 = TreeNode(x=4)
        cls.node5 = TreeNode(x=5)
        cls.root.left = cls.node2
        cls.root.right = cls.node3
        cls.node2.left = cls.node4
        cls.node2.right = cls.node5

    def test_get_path_to_target1(self) -> None:
        path = get_path_to_target(root=self.root, target=self.root)
        self.assertEqual(path, [1])