#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = self.helper(nums)
        return res

    def helper(self, nums):
        if len(nums) == 1:
            return [nums]

        j = 0
        res = []
        last_num = nums[0] - 1
        while j < len(nums):
            num = nums[j]
            if num == last_num:
                j += 1
                continue
            for item in self.helper(nums[:j] + nums[j + 1:]):
                res.append([num] + item)
            j += 1
            last_num = num
        return res
# @lc code=end

