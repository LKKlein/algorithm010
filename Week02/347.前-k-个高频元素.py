#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start

from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for num in nums:
            data[num] = data.get(num, 0) + 1
        h = []
        for num, count in data.items():
            heappush(h, [-count, num])
        return [heappop(h)[1] for i in range(k)]
# @lc code=end

