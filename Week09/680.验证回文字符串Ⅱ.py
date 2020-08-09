class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        p, q = 0, n - 1
        while p < q:
            if s[p] != s[q]:
                return self.isPalindrome(s, p + 1, q) or self.isPalindrome(s, p, q - 1)
            else:
                p += 1
                q -= 1
        return True

    def isPalindrome(self, s, p, q):
        while p < q:
            if s[p] != s[q]: return False
            else:
                p += 1
                q -= 1
        return True
