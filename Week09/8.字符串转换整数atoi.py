class Solution:
    def __init__(self):
        self.num = {str(i): i for i in range(10)}
        self.int_max = 2**31 - 1
        self.int_min = -2**31

    def myAtoi(self, S: str) -> int:
        S = S.strip()
        if not S: return 0
        S = " " + S + " "
        start = 0
        s = ""
        for ind, s in enumerate(S):
            if start == 0 and (s == "-" or s == "+" or s.isdigit()):
                start = ind
            elif start != 0 and (not s.isdigit()):
                s = S[start:ind]
                break
            elif start == 0 and s != " " and s != "+" and s != "-" and not s.isdigit():
                return 0
        ans = self.atoi(s)
        if ans > self.int_max:
            return self.int_max
        elif ans < self.int_min:
            return self.int_min
        else:
            return ans
            
    def atoi(self, s):
        if not s: return 0
        if s.startswith("-"): return 0 - self.atoi(s[1:])
        if s.startswith("+"): return self.atoi(s[1:])
        return self.num[s[0]] * (10 ** (len(s) - 1)) + self.atoi(s[1:])
