class Solution(object):
    def validPalindrome(self, s):
        def ispal(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return ispal(left+1,right) or ispal(left,right-1)
        return True
                     
        """
        :type s: str
        :rtype: bool
        """
        