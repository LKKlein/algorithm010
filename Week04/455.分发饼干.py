#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    # def findContentChildren(self, g: List[int], s: List[int]) -> int:
    #     if len(g) == 0 or len(s) == 0: return 0
    #     g.sort()
    #     s.sort()
    #     ans = 0
    #     for gi in g:
    #         found = False
    #         while len(s) > 0:
    #             si = s.pop(0)
    #             if si >= gi:
    #                 found = True
    #                 ans += 1
    #                 break
    #         if not found:
    #             break
    #     return ans

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        ind = 0
        for si in s:
            if ind == len(g):
                break
            if si >= g[ind]:
                ans += 1
                ind += 1
        return ans
# @lc code=end

