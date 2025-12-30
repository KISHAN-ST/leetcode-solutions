class Solution(object):
    def lengthOfLastWord(self, s):
        sub=s.split()
        return len(sub[-1])
        """
        :type s: str
        :rtype: int
        """
        