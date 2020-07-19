# 状态表：二维矩阵，到达每个点的最小路径
# 状态边界：第一行、第一列均为累加和
# 状态转移：左、上两个方向的最小值与当前值相加
#  dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    #     if not grid or not grid[0]: return 0
    #     m, n = len(grid), len(grid[0])
    #     dp = [[0] * n for _ in range(m)]
    #     dp[0][0] = grid[0][0]
    #     for i in range(1, n):
    #         dp[0][i] = grid[0][i] + dp[0][i - 1]
    #     for i in range(1, m):
    #         dp[i][0] = grid[i][0] + dp[i - 1][0]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    #     return dp[m - 1][n - 1]

    # 动态规划，修改原数组
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
