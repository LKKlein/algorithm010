#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
# [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
class Solution:
    def jump(self, nums: List[int]) -> int:
        m, start, max_pos, step = len(nums), 0, 0, 0
        for i, num in enumerate(nums[:-1]):
            if max_pos < num + i: max_pos = num + i
            if i == start:
                start = max_pos
                step += 1
        return step
# @lc code=end

