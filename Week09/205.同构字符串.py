class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ss = {}
        ss2 = {}
        for a, b in zip(s, t):
            if a not in ss:
                ss[a] = b
            else:
                if b != ss[a]:
                    return False

            if b not in ss2:
                ss2[b] = a
            else:
                if a != ss2[b]:
                    return False
        return True
