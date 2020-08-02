class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     if n <= 0: return False
    #     while n > 1:
    #         if n % 2 == 1:
    #             return False
    #         n = n >> 1
    #     return True

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
