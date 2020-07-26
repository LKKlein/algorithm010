class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.generate(n, n, "")
        return self.ans
        
    def generate(self, left, right, path):
        if left == 0 and right == 0:
            self.ans.append(path)
            return
        
        if left > 0:
            self.generate(left - 1, right, path + "(")
        
        if right > left:
            self.generate(left, right - 1, path + ")")
