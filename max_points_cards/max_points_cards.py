from typing import List

def maxScore(cardPoints: List[int], k: int) -> int:
    L = len(cardPoints) - 1
    max_sum = sum(cardPoints[:k])
    curr_sum = max_sum
    for i in range(k):
        curr_sum = curr_sum - cardPoints[k-1-i] + cardPoints[L-i]
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        return maxScore(cardPoints, k)


if __name__ == "__main__":
    cardPoints = [1,2,3,4,5,6,1] 
    k = 3
    out = maxScore(cardPoints, k)
    print(out)
