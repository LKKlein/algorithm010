#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            res = target - num
            if res in d:
                return [d[res], idx]
            d[num] = idx
        return [0, 0]
# @lc code=end

