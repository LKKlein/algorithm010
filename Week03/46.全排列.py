#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        j = 0
        res = []
        while j < len(nums):
            num = nums[j]
            for item in self.permute(nums[:j] + nums[j + 1:]):
                res.append([num] + item)
            j += 1
        return res

    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     if len(nums) == 1:
    #         return [nums]
        
    #     res = []
    #     for j in range(len(nums)):
    #         for item in self.permute(nums[:j] + nums[j + 1:]):
    #             res.append([nums[j]] + item)
    #     return res
# @lc code=end

