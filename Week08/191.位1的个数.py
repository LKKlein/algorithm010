class Solution:
    # %2
    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n > 0:
    #         if n % 2 == 1: count += 1
    #         n = n // 2
    #     return count

    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n > 0:
    #         if n & 1 == 1: count += 1
    #         n = n >> 1
    #     return count

    # def hammingWeight(self, n: int) -> int:
    #     count = 0
    #     while n > 0:
    #         count += 1
    #         n = n & (n - 1)  # 清除最右边的 1
    #     return count

    def hammingWeight(self, n: int) -> int:
        return bin(n).count("1")
