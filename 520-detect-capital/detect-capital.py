class Solution(object):
    def detectCapitalUse(self, word):
        if word[0].isupper() and word[1:].islower():
            return True
        elif word.islower():
            return True
        else:
            return word.isupper()
        """
        :type word: str
        :rtype: bool
        """
        