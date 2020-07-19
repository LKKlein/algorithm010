# 动态规划
# 状态表：二维矩阵，每个点能构成的最大正方形的边长
# 状态边界：第一行、第一列就是矩阵本身第一行、第一列的值
# 状态转移：当前点为1，则根据左上角三个值的最小值来判断能否继续构成更大的正方形
# dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1, if matrix[i][j] = 1
# dp[i][j] = 0, if matrix[i][j] = 0

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: return 0
        max_num = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                max_num = max(max_num, dp[i][j])
        return max_num * max_num
