#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     s = [[]]
    #     for num in nums:
    #         s += [item + [num] for item in s]
    #     return s

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        res.append(path)
        for idx, num in enumerate(nums):
            self.dfs(nums[idx+1:], path + [num], res)
# @lc code=end

