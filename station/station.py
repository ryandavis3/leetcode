from typing import List

# https://leetcode.com/problems/gas-station/

def subtract(x: List[int], y: List[int]) -> List[int]:
    """
    Subtract vector y from vector x.
    """
    L = len(x)
    z = [0] * L
    for i in range(L):
        z[i] = x[i] - y[i]
    return z

def cumsum(x: List[int]) -> List[int]:
    """
    Cumulative sum of vector x.
    """
    L = len(x)
    z = [0] * L
    z[0] = x[0]
    for i in range(1, L):
        z[i] = z[i-1] + x[i]
    return z

def circuit(gas: List[int], cost: List[int]) -> int:
    """
    Return index allowing us to travel around circuit once
    in clockwise direction. If we cannot travel around circuit,
    return -1.
    """
    diff = subtract(gas, cost)
    # More cost than gas available
    if sum(diff) < 0:
        return -1
    # Find starting gas station index
    cumDiff = cumsum(diff) 
    minDiff = min(cumDiff) 
    index = cumDiff.index(minDiff)
    L = len(diff)
    index = (index + 1) % L
    return index


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        return circuit(gas, cost)
