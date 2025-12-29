class Solution(object):
    def findTheDifference(self, s, t):
       freq={}
       for ch in t:
        freq[ch]=freq.get(ch,0)+1
       for ch in s:
        freq[ch]-=1
       for ch in freq:
        if freq[ch]==1:
            return ch
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        