# 状态表：一维向量，每个节点存储当前这个节点能构成多少个回文字符串
# 状态边界： dp[0] = 1
# 状态转移： 前一个节点能构成的回文字符串数量 加上 包含当前字符能构成的回文字符数量
#  dp[n] = dp[n - 1] + cur

class Solution:
    # def countSubstrings(self, s: str) -> int:
    #     n = len(s)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         cur = 1
    #         for j in range(i):
    #             ch = s[j:i+1]
    #             if ch == ch[::-1]:
    #                 cur += 1
    #         dp[i] = dp[i - 1] + cur
    #     return dp[n - 1]

    # 中心扩展法
    def countSubstrings(self, s: str) -> int:
        ans, n = 0, len(s)
        for center in range(2 * n - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < n and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans
