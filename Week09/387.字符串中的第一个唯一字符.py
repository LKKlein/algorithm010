class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import OrderedDict
        ss = OrderedDict()
        for ind, c in enumerate(s):
            if c not in ss:
                ss[c] = [1, ind]
            else:
                ss[c] = [ss[c][0] + 1, ss[c][1]]
        for cnt, ind in ss.values():
            if cnt == 1:
                return ind
        return -1
