def countVowelStrings(n: int) -> int:
    # Degenerate case -> return zero
    if n == 0:
        return 0
    # Case with n = 1
    V = ["1", "2", "3", "4", "5"]
    l = 1
    # Iterate over lengths of strings
    while l < n:
        # Iterate over strings
        Vl = []
        for s in V:
            Vs = [s+str(i) for i in range(int(s[-1]), 6)]
            Vl += Vs
        V = Vl
        l += 1
    return V


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return len(countVowelStrings(n))

if __name__ == "__main__":
    V1 = countVowelStrings(1)
    print(V1)
    V2 = countVowelStrings(2)
    print(V2)
    V3 = countVowelStrings(3)
    print(V3)

