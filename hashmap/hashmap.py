# https://leetcode.com/problems/design-hashmap/

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.D = dict()
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.D[key] = value
    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key not in self.D:
            return -1
        return self.D[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.D:
            del self.D[key]

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
