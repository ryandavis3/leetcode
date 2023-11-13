from typing import Dict, List, Optional
from unittest import TestCase


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_path_to_target(root: TreeNode, target: TreeNode) -> Optional[List[int]]:
    if root.val == target.val:
        return [root.val]
    if root.left:
        left_path = get_path_to_target(root=root.left, target=target)
        if left_path is not None:
            return [root.val] + left_path
    if root.right:
        right_path = get_path_to_target(root=root.right, target=target)
        if right_path is not None:
            return [root.val] + right_path
    return None


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

    def test_get_path_to_target2(self) -> None:
        path = get_path_to_target(root=self.root, target=self.node4)
        self.assertEqual(path, [1, 2, 4])

    def test_get_path_to_target3(self) -> None:
        path = get_path_to_target(root=self.root, target=self.node5)
        self.assertEqual(path, [1, 2, 5])

    def test_get_path_to_target4(self) -> None:
        path = get_path_to_target(root=self.root, target=self.node3)
        self.assertEqual(path, [1, 3])