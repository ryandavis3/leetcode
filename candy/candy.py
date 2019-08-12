import multiprocessing
import signal
from typing import List

# https://leetcode.com/problems/candy/

## BACKTRACKING SOLUTION

def candy(ratings: List[int], prev_candy: int, prev_rating: int):
    """
    There are N children standing in a line. Each child is 
    assigned a rating value. Each child must have one candy. 
    Children with a higher rating get more candies than their
    neighbors. Find the minimum candies we must give. Use backtracking.
    """
    # Completed line! No more candies needed!
    if not ratings:
        return 0
    rating = ratings[0]
    # Previous child rated higher and gets more candy.
    if prev_rating > rating:
        n_candy = 1
        while True:
            # Return -1 if current child gets equal or
            # more candy than previous child.
            if prev_candy <=  n_candy:
                return -1
            # Recurse on smaller group
            solution = candy(ratings[1:], n_candy, rating)
            # If valid solution, return it
            if solution >= 0:
                return n_candy + solution
            # Increment number of candies
            n_candy += 1
    if prev_rating == rating:
        n_candy = 1
    else: # Current child get more candy than previous child 
        n_candy = prev_candy + 1
    while True:
        # Recurse on smaller group
        solution = candy(ratings[1:], n_candy, rating)
        # If valid solution, return it
        if solution >= 0:
            return n_candy + solution
        # Increment number of candies
        n_candy += 1    

# Handle timeouts
class timeout:
    def __init__(self, seconds=1, error_message='Timeout'):
        self.seconds = seconds
        self.error_message = error_message
    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)
    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)
    def __exit__(self, type, value, traceback):
        signal.alarm(0)

def candyTime(ratings: List[int], reverse: bool):
    """
    Solve with one second timeout.
    """
    if reverse:
        ratings = list(reversed(ratings))
    try:
        with timeout(seconds=1):
            result = candy(ratings, 0, -100)
            return result
    except TimeoutError:
        return -1

def solve(ratings: List[int]) -> int:
    """
    Try solving in both left-ro-right and right-to-left
    directions.
    """
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    results = [pool.apply(candyTime, args=(ratings, rev)) for rev in [0,1]]
    return max(results)

class Solution:
    def candy(self, ratings: List[int]) -> int:
        return solve(ratings) 

## LEETCODE SOLUTION: TWO ARRAYS

def candyTwoArrays(ratings: List[int]):
    """
    Use two arrays with left (right) passes to find minimum
    number of candies.
    """
    # Left to right pass
    L = len(ratings)
    left = [1] * L
    for i in range(1, L):
        if ratings[i] > ratings[i-1]:
            left[i] = left[i-1] + 1
    # Right to left pass
    right = [1] * L
    for i in range(L-1, 0, -1):
        if ratings[i-1] > ratings[i]:
            right[i-1] = right[i] + 1
    # Combine right and left passes
    combined = [max(left[i], right[i]) for i in range(L)]
    # Compute total number of candies
    return sum(combined)
















