class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        for i in range(n):
            if board[0][i] == "O":
                self.findAll(board, 0, i)
            if board[m - 1][i] == "O":
                self.findAll(board, m - 1, i)

        for i in range(1, m - 1):
            if board[i][0] == "O":
                self.findAll(board, i, 0)
            if board[i][n - 1] == "O":
                self.findAll(board, i, n - 1)

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O":
                    board[i][j] = "X"
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"

    def findAll(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "X" or board[i][j] == "#":
            return
        board[i][j] = "#"
        self.findAll(board, i - 1, j)
        self.findAll(board, i + 1, j)
        self.findAll(board, i, j - 1)
        self.findAll(board, i, j + 1)
