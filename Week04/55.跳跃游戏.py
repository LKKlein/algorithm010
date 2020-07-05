#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    # def canJump(self, nums: List[int]) -> bool:
    #     if not nums: return False
    #     m = len(nums)
    #     canReachable = 0
    #     for i, num in enumerate(nums):
    #         if canReachable >= m - 1 or i > canReachable:
    #             break
    #         if canReachable < i + num:
    #             canReachable = i + num
    #     return canReachable >= m - 1

    def canJump(self, nums: List[int]) -> bool:
        if not nums: return False
        m = len(nums)
        canReachable = m - 1
        for i in range(m - 1, -1, -1):
            if nums[i] + i >= canReachable:
                canReachable = i
        return canReachable == 0
# @lc code=end

