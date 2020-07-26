class Solution:
    def climbStairs(self, n: int) -> int:
        lookup = {}
        return self.backtrace(n, lookup)

    def backtrace(self, n, lookup):
        if n <= 2:
            return n
        if n not in lookup:
            lookup[n] = self.backtrace(n - 1, lookup) + self.backtrace(n - 2, lookup)
        return lookup[n]
