class Solution(object):
    def removePalindromeSub(self, s):
        if not s:
            return 0
        elif s==s[::-1]:
            return 1
        else:
            return 2
        

           
        """
        :type s: str
        :rtype: int
        """
        