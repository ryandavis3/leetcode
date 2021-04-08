def countArrangement(n: int) -> int:
    
    S = set(range(1, n+1))

    def backtrack(N: int, S) -> int:
        
        # First position!
        if N == 1:
            return 1
            
        # Try each element in S in position
        total = 0
        for i in S:
            if N % i == 0 or i % N == 0:
                total += backtrack(N-1, S-{i})
        
        return total
        
    total = backtrack(n, S)

    return total


class Solution:
    def countArrangement(self, n: int) -> int:
        return countArrangement(n)


if __name__ == "__main__":
    n = 2
    result = countArrangement(n)
    print(result)
    n = 3
    result1 = countArrangement(n)
    print(result1)
    n = 4
    result2 = countArrangement(n)
    print(result2)
