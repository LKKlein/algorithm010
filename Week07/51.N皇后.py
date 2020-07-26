class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        pq_plus, pq_diff, col = [], [], []
        self.ans = []
        self.backtrace(n, 0, pq_plus, pq_diff, col, [])
        return self.ans

    def backtrace(self, n, i, pq_plus, pq_diff, cols, path):
        if i == n:
            self.ans.append(path)
            return
        for j in range(n):
            if i + j not in pq_plus and i - j not in pq_diff and j not in cols:
                res = ["."] * n
                res[j] = "Q"
                self.backtrace(n, i + 1, pq_plus + [i + j], pq_diff + [i - j], cols + [j], path + ["".join(res)])
