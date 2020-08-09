class Solution:
    # def reverseWords(self, s: str) -> str:
    #     ss = [c[::-1] for c in s.split()]
    #     return " ".join(ss)

    # def reverseWords(self, s: str) -> str:
    #     start, end = 0, 0
    #     ss = ""
    #     for ind, c in enumerate(s, 1):
    #         if c == " ":
    #             if end != 0:
    #                 ss += s[start:end][::-1] + " "
    #                 end = 0
    #             start = ind
    #         else:
    #             end = ind
    #     if end != 0:
    #         ss += s[start:end][::-1] + " "
    #     return ss[:-1]

    def reverseWords(self, s: str) -> str:
        stack, ss = [], ""
        for c in s:
            if c == " ":
                while stack:
                    ss += stack.pop()
                ss += " "
            else:
                stack.append(c)
        while stack:
            ss += stack.pop()
        return ss
