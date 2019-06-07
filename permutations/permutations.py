from typing import List, Set

# https://leetcode.com/problems/permutations/

class Permutation:
    """
    Class representing a single permutation
    """
    def __init__(self, L: List, R: Set):
        """
        Constuctor. L is the permutation and R is
        a set of remaining digits. 
        """
        self.L = L
        self.R = R

    def extend(self):
        """
        Create a set of new permutations by extending 
        the existing permutation by each of the remaining
        letters separately.
        """
        perms = []
        R = self.R.copy()
        for letter in R:
            Rn = R.copy()
            Rn.remove(letter)
            Ln = self.L + [letter]
            perms += [Permutation(Ln, Rn)]
        return perms

    def permLen(self):
        """
        Get length of permutation. 
        """
        return len(self.L)


def permute(nums: List[int]) -> List[List[int]]:
    """
    Given a collection of distinct integers, return
    all possible permutations.
    """
    L = []
    N = len(nums)
    R = set(nums)
    perms = [Permutation(L, R)]
    # Continue to extend each permutation until no letters
    # are left.
    while perms[0].permLen() < N:
        permsn = []
        for perm in perms:
            permsn += perm.extend()
        perms = permsn
    # Represent each permutation as list of int 
    perms = [perm.L for perm in perms]
    return perms

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return permute(nums)
