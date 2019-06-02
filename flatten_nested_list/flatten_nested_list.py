# https://leetcode.com/problems/flatten-nested-list-iterator

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        # Define local function to flatten list.
        def flatten(nestedList):
            """
            Use a recursive approach to flatten a nested list.
            """
            # Initialize empty list
            flatList = []
            for val in nestedList:
                # If value is integer, add it to flat list
                if val.isInteger():
                    flatList += [val.getInteger()]
                # If value is list, recursively call flatten
                # and add the result to flat list
                else:
                    flatList += flatten(val.getList())
            return flatList
        # Flatten list, store index and length of list
        self.flatList = flatten(nestedList)
        self.index = 0
        self.L = len(self.flatList)

    def next(self):
        """
        :rtype: int
        """
        val = self.flatList[self.index]
        self.index += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.L

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
