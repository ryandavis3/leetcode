def nthUglyNumber(n: int) -> int:
    nums = [1, 2, 3, 4, 5]
    if n <= 5:
        return nums[n-1]
    ugly = 5
    i = 6
    uglies = {1, 2, 3, 4, 5}
    while ugly < n:
        if i / 2 in uglies or i / 3 in uglies or i / 5 in uglies:
            uglies.add(i)
            ugly += 1
        i += 1
    return i - 1 


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return nthUglyNumber(n)

if __name__ == "__main__":
    xx = nthUglyNumber(470)
    print(xx)
