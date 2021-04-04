def countVowelStrings(n: int) -> int:
    if n == 1:
        return 5
    table = []
    for i in range(n):
        table += [[None] * 5]
    for i in range(n):
        for j in range(5):
            if i == 0:
                table[i][j] = 1
            elif j == 0:
                table[i][j] = 1
            else:
                table[i][j] = table[i][j-1] + table[i-1][j]
    total = 0
    for j in range(5):
        total += table[i][j]
    return total


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return countVowelStrings(n)

if __name__ == "__main__":
    V1 = countVowelStrings(1)
    print(V1)
    V2 = countVowelStrings(2)
    print(V2)
    V3 = countVowelStrings(3)
    print(V3)

