class Solution(object):
    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        
        res = ""
        for i in range(len(s)):
            # Odd length palindrome
            p1 = self.expand(s, i, i)
            # Even length palindrome
            p2 = self.expand(s, i, i + 1)
            
            # Update result
            res = max(res, p1, p2, key=len)
        
        return res

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
