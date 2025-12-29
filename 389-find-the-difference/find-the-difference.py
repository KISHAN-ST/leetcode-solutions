class Solution(object):
    def findTheDifference(self, s, t):
       result=0

       for ch in t:
        result^=ord(ch)

       for ch in s:
        result^=ord(ch)
       return chr(result)

        