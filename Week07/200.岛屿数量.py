class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.fillIslands(grid, i, j)
        return count

    def fillIslands(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.fillIslands(grid, i - 1, j)
        self.fillIslands(grid, i + 1, j)
        self.fillIslands(grid, i, j - 1)
        self.fillIslands(grid, i, j + 1)
