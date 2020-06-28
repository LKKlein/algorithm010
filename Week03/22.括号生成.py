#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n):
        res = []
        self.helper(0, 0, n, "", res)
        return res

    def helper(self, left, right, total, s, res):
        if left + right >= 2 * total:
            res.append(s)
            return

        if left < total:
            self.helper(left + 1, right, total, s + "(", res)
        if right < left:
            self.helper(left, right + 1, total, s + ")", res)
# @lc code=end

