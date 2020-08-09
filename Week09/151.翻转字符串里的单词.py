class Solution:
    # def reverseWords(self, s: str) -> str:
    #     ss = s.split()
    #     return " ".join(ss[::-1])

    def reverseWords(self, s: str) -> str:
        ss = ""
        start = 0
        end = 0
        for ind, c in enumerate(s, 1):
            if c == " ":
                if end != 0:
                    ss = s[start: end] + " " + ss
                    end = 0
                start = ind
            else:
                end = ind
        if end != 0:
            ss = s[start: end] + " " + ss
        return ss[:-1]
