# 动态规划
# 状态表： 一维向量，存储每个从起始到当前位置，能解码的数量
# 状态边界：dp[0] = 1, dp[1] = 1 (if s[:2] > 26), dp[1] = 2 (else)
# 状态转移：
# dp[i] = dp[i - 1], if s[i - 1] != 0
# dp[i] = dp[i - 1] + dp[i - 2], if 26 >= s[i - 2: i] >= 10


class Solution:
    # 回溯， 绝对超时
    # def numDecodings(self, s: str) -> int:
    #     if not s: return 1
    #     num = self.numDecodings(s[1:])
    #     if len(s) >= 2:
    #         if s[0] == "1" or (s[0] == "2" and s[1] not in ["7", "8", "9"]):
    #             num += self.numDecodings(s[2:])
    #     return num

    # 动态规划，即有限制的爬楼梯
    # def numDecodings(self, s: str) -> int:
    #     if s[0] == "0": return 0
    #     dp = [0] * len(s)
    #     dp[-1] = 1
    #     dp[0] = 1

    #     for i in range(1, len(s)):
    #         if ((s[i - 1] == "1" and s[i] != "0") or (s[i - 1] == "2" and s[i] not in ["0", "7", "8", "9"])) and ((i + 1 < len(s) and s[i + 1] != "0") or i == len(s) - 1):
    #             dp[i] = dp[i - 1] + dp[i - 2]
    #         elif s[i] == "0" and s[i - 1] != "1" and s[i - 1] != "2":
    #             return 0
    #         else:
    #             dp[i] = dp[i - 1]
    #     return dp[-1]

    def numDecodings(self, s: str) -> int:
        if s[0] == "0": return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(1, n):
            if s[i] != "0":
                dp[i + 1] = dp[i]
            if s[i - 1:i + 1] >= "10" and s[i - 1: i + 1] <="26":
                dp[i + 1] += dp[i - 1]
        return dp[-1]
