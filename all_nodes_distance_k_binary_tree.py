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


def get_distance_dict(path: List[int]) -> Dict[int, int]:
    path_reversed = path[::-1]
    distance_dict: Dict[int, int] = {}
    for i, val in enumerate(path_reversed):
        distance_dict[val] = i
    return distance_dict


def fill_all_distance_dict(root: TreeNode, distance_dict: Dict[int, int]) -> None:
    root_distance = distance_dict[root.val]
    if root.left:
        if root.left.val not in distance_dict:
            distance_dict[root.left.val] = root_distance + 1
        fill_all_distance_dict(root=root.left, distance_dict=distance_dict)
    if root.right:
        if root.right.val not in distance_dict:
            distance_dict[root.right.val] = root_distance + 1
        fill_all_distance_dict(root=root.right, distance_dict=distance_dict)


def get_distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    path_to_target = get_path_to_target(root=root, target=target)
    distance_dict = get_distance_dict(path=path_to_target)
    fill_all_distance_dict(root=root, distance_dict=distance_dict)
    distance_k_nodes = [val for val, dist in distance_dict.items() if dist == k]
    return distance_k_nodes


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        return get_distance_k(root=root, target=target, k=k)


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

    def test_get_distance_dict1(self) -> None:
        path = [1, 2, 4]
        _dict = get_distance_dict(path=path)
        expected_dict = {4: 0, 2: 1, 1: 2}
        self.assertEqual(_dict, expected_dict)

    def test_fill_all_distance_dict1(self) -> None:
        distance_dict = {4: 0, 2: 1, 1: 2}
        fill_all_distance_dict(root=self.root, distance_dict=distance_dict)
        expected_distance_dict = {4: 0, 2: 1, 1: 2, 5: 2, 3: 3}
        self.assertEqual(distance_dict, expected_distance_dict)

    def test_get_distance_k1(self) -> None:
        distance_2 = get_distance_k(root=self.root, target=self.node4, k=2)
        self.assertEqual(distance_2, [1, 5])