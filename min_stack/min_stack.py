import unittest
import uuid
from typing import Optional


class Node:
    def __init__(self, value: int, prev):
        self.value = value
        self.prev = prev
        self.uuid = str(uuid.uuid4())


class MinStack:

    def __init__(self):
        self._head = None

    def push(self, val: int) -> None:
        node = Node(value=val, prev=self._head)
        self._head = node

    def pop(self) -> None:
        if self._head is None:
            raise ValueError('No head available!')
        self._head = self._head.prev

    def top(self) -> int:
        if self._head is None:
            raise ValueError('No head available!')
        top_value = self._head.value
        return top_value

    def getMin(self) -> int:
        # Get the minimum element in the stack
        pass

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class TestMinStack(unittest.TestCase):

    def test_top(self) -> None:
        stack = MinStack()
        stack.push(val=1)
        stack.push(val=2)
        top = stack.top()
        self.assertEqual(top, 2)
        stack.pop()
        top = stack.top()
        self.assertEqual(top, 1)

