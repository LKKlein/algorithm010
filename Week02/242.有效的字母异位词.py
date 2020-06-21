#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for w in s:
            d[w] = d.get(w, 0) + 1
        for w in t:
            if w not in d:
                return False
            d[w] -= 1
        return all([i == 0 for i in d.values()])
# @lc code=end

