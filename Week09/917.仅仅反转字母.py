class Solution:
    # def reverseOnlyLetters(self, S: str) -> str:
    #     ss = list(S)
    #     p, q = 0, len(S) - 1
    #     fp, fq = False, False
    #     while p < q:
    #         if not fp:
    #             op = ord(ss[p])
    #             if (op >=97 and op <= 122) or (op >=65 and op <= 90):
    #                 fp = True
    #             else:
    #                 fp = False
    #                 p += 1
    #                 continue

    #         if not fq:
    #             oq = ord(ss[q])
    #             if (oq >=97 and oq <= 122) or (oq >=65 and oq <= 90):
    #                 fq = True
    #             else:
    #                 fq = False
    #                 q -= 1
    #                 continue
            
    #         if fp and fq:
    #             ss[p], ss[q] = ss[q], ss[p]
    #             p += 1
    #             q -= 1
    #             fp, fq = False, False
    #     return "".join(ss)

    def reverseOnlyLetters(self, S: str) -> str:
        ss = list(S)
        p, q = 0, len(S) - 1
        fp, fq = False, False
        while p < q:
            if not fp:
                if ss[p].isalpha():
                    fp = True
                else:
                    fp = False
                    p += 1
                    continue

            if not fq:
                if ss[q].isalpha():
                    fq = True
                else:
                    fq = False
                    q -= 1
                    continue
            
            if fp and fq:
                ss[p], ss[q] = ss[q], ss[p]
                p += 1
                q -= 1
                fp, fq = False, False
        return "".join(ss)

    # def reverseOnlyLetters(self, S: str) -> str:
    #     letters = [c for c in S if c.isalpha()]
    #     ans = []
    #     for c in S:
    #         if c.isalpha():
    #             ans.append(letters.pop())
    #         else:
    #             ans.append(c)
    #     return "".join(ans)
