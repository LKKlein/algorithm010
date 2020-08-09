ass Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ss = ""
        x = 2 * k
        for i in range(0, len(s), k):
            if i % x == 0:
                ss += s[i:i+k][::-1]
            else:
                ss += s[i:i+k]
        return ss
