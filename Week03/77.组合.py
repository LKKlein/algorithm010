#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0:
            return [[]]
        res = self.helper(list(range(1, n + 1)), k)
        return res

    def helper(self, nums, k):
        if len(nums) == 0 or k == 0:
            return [[]]
        j = 0
        res = []
        while j < len(nums) - k + 1:
            num = nums[j]
            for item in self.helper(nums[j + 1:], k - 1):
                res.append([num] + item)
            j += 1
        return res
# @lc code=end

