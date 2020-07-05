#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.bfs_marker(grid, i, j)
                    count += 1
        return count

    # def dfs_marker(self, grid, i, j):
    #     if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != "1":
    #         return
    #     grid[i][j] = 0
    #     self.dfs_marker(grid, i - 1, j)
    #     self.dfs_marker(grid, i + 1, j)
    #     self.dfs_marker(grid, i, j - 1)
    #     self.dfs_marker(grid, i, j + 1)

    def bfs_marker(self, grid, x, y):
        from collections import deque
        queue = deque([(x, y)])
        while queue:
            i, j = queue.popleft()
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] != "1":
                continue
            grid[i][j] = 0
            queue.append([i + 1, j])
            queue.append([i - 1, j])
            queue.append([i, j + 1])
            queue.append([i, j - 1])
# @lc code=end

