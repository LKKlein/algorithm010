class Solution:
    str2int = {
        "1": 1, "2": 2, "3": 3,
        "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9,
    }

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        blocks = [[False] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    ind = self.str2int[board[i][j]] - 1
                    rows[i][ind] = True
                    cols[j][ind] = True
                    block = 3 * (i // 3) + j // 3
                    blocks[block][ind] = True
        self.dfs(board, rows, cols, blocks, 0, 0)

    def dfs(self, board, rows, cols, blocks, i, j):
        # 先找到一个空位，如果没有空位了就直接返回
        while board[i][j] != ".":
            j += 1
            if j >= 9:
                i, j = i + 1, 0
            if i >= 9:
                return True
    
        for k in range(9):
            block = 3 * (i // 3) + j // 3
            if not rows[i][k] and not cols[j][k] and not blocks[block][k]:
                board[i][j] = str(k + 1)
                rows[i][k] = True
                cols[j][k] = True
                blocks[block][k] = True
                if self.dfs(board, rows, cols, blocks, i, j):
                    return True
                else:
                    board[i][j] = "."
                    rows[i][k] = False
                    cols[j][k] = False
                    blocks[block][k] = False

        return False
