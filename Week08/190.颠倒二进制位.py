class Solution:
    def reverseBits(self, n: int) -> int:
        res, count = 0, 0
        while count < 32:
            res <<= 1  # res 左移一位空出位置
            res |= (n & 1)  # 得到的最低位加过来
            n >>= 1  # 原数字右移一位去掉已经处理过的最低位
            count += 1
        return res

