class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]: return 0
        count = 0
        n = len(M)
        visited = set()
        for i in range(n):
            if i in visited: continue
            count += 1
            self.dfs_helper(M, i, visited)
        return count

    def dfs_helper(self, M, i, visited):
        if i in visited: return
        visited.add(i)
        for k in range(len(M)):
            if M[i][k] == 1:
                M[i][k] = 0
                self.dfs_helper(M, k, visited)
