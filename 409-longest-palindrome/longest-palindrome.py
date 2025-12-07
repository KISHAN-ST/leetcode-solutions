class Solution(object):
    def longestPalindrome(self, s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        length=0
        odd_found=False
        for count in freq.values():
            length+=(count//2)*2
            if count%2==1:
                odd_found=True
        if odd_found==True:
            length+=1
        return length
            
        """
        :type s: str
        :rtype: int
        """
        