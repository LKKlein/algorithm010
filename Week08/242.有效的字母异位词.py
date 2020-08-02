class Solution:
    # def isAnagram(self, s: str, t: str) -> bool:
    #     d = {}
    #     for w in s:
    #         d[w] = d.get(w, 0) + 1
    #     for w in t:
    #         if w not in d:
    #             return False
    #         d[w] -= 1
    #     return all([i == 0 for i in d.values()])

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        s = str(sorted(s))
        t = str(sorted(t))
        if s == t: return True
        return False
