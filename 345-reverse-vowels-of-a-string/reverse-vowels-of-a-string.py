class Solution(object):
    def reverseVowels(self, s):
        vowel=set('aeiouAEIOU')
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            while left<right and not s[left] in vowel:
                left+=1
            while left<right and not s[right] in vowel:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return"".join(s)
        
        
        
        
        """
        :type s: str
        :rtype: str
        """
        